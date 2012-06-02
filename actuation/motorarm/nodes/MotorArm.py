#!/usr/bin/env python
from __future__ import division
import roslib; roslib.load_manifest('motorarm')
import rospy
import numpy as N
import serial
import tf
import threading
import PyKDL
from geometry_msgs.msg import Point, PointStamped, Pose, PoseStamped, Vector3
from sensor_msgs.msg import JointState
from std_msgs.msg import Header, ColorRGBA
from visualization_msgs.msg import Marker
from rosSimpleStep.srv import SrvCalibrate, SrvJointState, SrvSetZero
from flycore.msg import MsgFrameState
from flycore.srv import SrvFrameState, SrvFrameStateRequest, SrvFrameStateResponse
from patterngen.srv import SrvSignal, SrvSignalResponse


class MotorArm:

    def __init__(self):
        self.initialized = False
        self.initializedServices = False
        self.lock = threading.Lock()
        rospy.loginfo("Opening MotorArm device...")
        rospy.init_node('MotorArm')
        rospy.loginfo ("MotorArm name=%s", __name__)
        rospy.on_shutdown(self.OnShutdown_callback)

        self.names = ['joint1']
        self.jointstate1 = None
        
        # Publish & Subscribe
        rospy.Service('set_stage_state',    SrvFrameState, self.SetStageState_callback)
        rospy.Service('get_stage_state',    SrvFrameState, self.GetStageState_callback)
        rospy.Service('home_stage',         SrvFrameState, self.HomeStage_callback)
        rospy.Service('calibrate_stage',    SrvFrameState, self.Calibrate_callback)
        
        rospy.Service('signal_input',       SrvSignal,     self.SignalInput_callback) # For receiving input from a signal generator.


        self.subEndEffectorOffset = rospy.Subscriber('EndEffectorOffset', Point, self.EndEffectorOffset_callback)
        self.pubJointState        = rospy.Publisher('joint_states', JointState)
        self.pubEndEffector       = rospy.Publisher('EndEffector', MsgFrameState)
        self.pubMarker            = rospy.Publisher('visualization_marker', Marker)
        
        self.tfrx = tf.TransformListener()
        self.tfbx = tf.TransformBroadcaster()

        self.js = JointState()
        self.js.header.seq = 0
        self.js.header.stamp = rospy.Time.now()
        self.js.header.frame_id = "1"
        self.js.name = self.names
        #self.js.velocity = [0.0]
        
        self.ptsToolRefExternal = None #Point(0,0,0) # Where we want the "tool".
        self.ptsToolRef = None
        self.ptEeSense = Point(0,0,0)
        self.ptEeCommand = Point(0,0,0) # Where to command the end-effector.
        self.ptOffsetSense = Point(0,0,0) # Vector from end-effector to the "tool"
        self.ptToolRefClipped = Point(0,0,0) 
        self.ptContourSense = Point(0,0,0)
        self.ptContourError = Point(0,0,0)
        self.ptToolRefError = Point(0,0,0)
        self.ptEeRef = Point(0,0,0)
        self.ptEeError = Point(0,0,0)
        self.ptEeErrorPrev = Point(0,0,0)
        self.ptEeDerror = Point(0,0,0)
        self.ptEeIerror = Point(0,0,0)
        self.ptEeIerrorClipped = Point(0,0,0)
        self.ptAntiwindup = Point(0,0,0)
        
        self.unwind = 0.0
        self.thetaPrev = 0.0
        self.speedCommandTool = None 
        self.speedStageMax = rospy.get_param('motorarm/speed_max', 200.0)
        self.L1 = rospy.get_param('motorarm/L1', 9.9) # Length of link1
        self.timePrev = rospy.Time.now()

        # PID Gains & Parameters.
        self.kP = rospy.get_param('motorarm/kP', 1.0)
        self.kI = rospy.get_param('motorarm/kI', 0.0)
        self.kD = rospy.get_param('motorarm/kD', 0.0)
        self.maxI = rospy.get_param('motorarm/maxI', 40.0)
        self.kWindup = rospy.get_param('motorarm/kWindup', 0.0)


        
        self.request = SrvFrameStateRequest()
        #self.request.state.header.stamp = rospy.Time.now()
        self.request.state.header.frame_id = 'Stage'
        self.request.state.pose.position.x = 0.0
        self.request.state.pose.position.y = 0.0
        self.request.state.pose.position.z = 0.0


    def LoadServices(self):
        # Load joint1 services.
        # Wait for joint 1 to launch.
        stSrv = 'srvCalibrate_'+self.names[0]
        rospy.wait_for_service(stSrv)
        try:
            self.Calibrate_joint1 = rospy.ServiceProxy(stSrv, SrvCalibrate)
        except (rospy.ServiceException, IOError), e:
            rospy.loginfo ("MotorArm FAILED %s: %s"%(stSrv,e))

        stSrv = 'srvGetState_'+self.names[0]
        rospy.wait_for_service(stSrv)
        try:
            self.GetState_joint1 = rospy.ServiceProxy(stSrv, SrvJointState)
        except (rospy.ServiceException, IOError), e:
            rospy.loginfo ("MotorArm FAILED %s: %s"%(stSrv,e))

        stSrv = 'srvSetPositionAtVel_'+self.names[0]
        rospy.wait_for_service(stSrv)
        try:
            self.SetPositionAtVel_joint1 = rospy.ServiceProxy(stSrv, SrvJointState)
        except (rospy.ServiceException, IOError), e:
            rospy.loginfo ("MotorArm FAILED %s: %s"%(stSrv,e))

        stSrv = 'srvPark_'+self.names[0]
        rospy.wait_for_service(stSrv)
        try:
            self.Park_joint1 = rospy.ServiceProxy(stSrv, SrvJointState)
        except (rospy.ServiceException, IOError), e:
            rospy.loginfo ("MotorArm FAILED %s: %s"%(stSrv,e))

        stSrv = 'srvSetZero_'+self.names[0]
        rospy.wait_for_service(stSrv)
        try:
            self.SetZero_joint1 = rospy.ServiceProxy(stSrv, SrvSetZero)
        except (rospy.ServiceException, IOError), e:
            rospy.loginfo ("MotorArm FAILED %s: %s"%(stSrv,e))


        self.initializedServices = True
        

    def ClipPtMag (self, pt, magMax):
        magPt = N.linalg.norm([pt.x, pt.y, pt.z])
        if magPt > magMax:
            r = magMax / magPt
        else:
            r = 1.0
            
        return Point(r*pt.x, r*pt.y, r*pt.z)
            
        
    # Forward kinematics:  Get x,y from theta 1
    def GetXyFromTheta (self, angle):
        # Rotate the frames from centered to east-pointing. 
        x = self.L1*N.cos(angle)
        y = self.L1*N.sin(angle)

        return (x, y)
    
    
    # GetThetaFromXY()
    # Inverse Kinematics: Get theta 1 from the (x,y) end-effector position,
    # where (x,y) is in the  frame of the workspace center.
    #
    def GetThetaFromXy (self, x, y):
        
        theta = (N.arctan2(y,x) % (2.0*N.pi))+self.unwind
        
        if (theta-self.thetaPrev) > N.pi: # Clockwise across zero.
            theta -= 2.0*N.pi
            self.unwind -= 2.0*N.pi
            
        elif (theta-self.thetaPrev) < -N.pi: # CCW across zero.
            theta += 2.0*N.pi
            self.unwind += 2.0*N.pi 
        
        self.thetaPrev = theta
        
        #rospy.logwarn('theta=%0.2f, unwind=%0.2f' % (theta, self.unwind))
        return theta
        
        
    
    def GetStageState_callback(self, reqStageState):
        state = self.GetStageState()
        return state
    
    def GetStageState (self):
        while not self.initializedServices:
            rospy.sleep(0.1)
            
        x = 0.0
        y = 0.0
        

        rvStageState = SrvFrameStateResponse()
        if (self.jointstate1 is not None):                    
            #rospy.loginfo ('MotorArm self.jointstate1=%s' % self.jointstate1)
            #(x,y) = self.GetXyFrom12 (self.jointstate1.position, self.jointstate2.position)
            
            # Transform the point into the requested frame.
            pt = Point()
            pt.x = self.ptEeSense.x + self.ptOffsetSense.x 
            pt.y = self.ptEeSense.y + self.ptOffsetSense.y 
            pt.z = self.ptEeSense.z + self.ptOffsetSense.z 
            
            #rvStageState.state.header.stamp = rospy.Time.now()
            rvStageState.state.header.frame_id = 'Stage' # Always return Stage frame coordinates.
            rvStageState.state.pose.position.x = pt.x 
            rvStageState.state.pose.position.y = pt.y 
            rvStageState.state.pose.position.z = pt.z
            rvStageState.state.velocity.linear.x = 0.0 # BUG: This should come from the hardware.
            rvStageState.state.velocity.linear.y = 0.0 # BUG: This should come from the hardware.
            rvStageState.state.velocity.linear.z = 0.0 # BUG: This should come from the hardware.
            rvStageState.state.velocity.angular.x = 0.0 # BUG: This should come from the hardware.
            rvStageState.state.velocity.angular.y = 0.0 # BUG: This should come from the hardware.
            rvStageState.state.velocity.angular.z = 0.0 # BUG: This should come from the hardware.
        
        return rvStageState.state

        
    # SetStageState_callback()
    #   Updates the target command.
    #
    def SetStageState_callback(self, reqStageState):
        while not self.initialized:
            rospy.sleep(0.5)
            
        #rospy.loginfo ('MotorArm SetStageState_callback req=%s' % reqStageState)
        
        #rospy.loginfo ('MotorArm SetStageState_callback Request x,y=%s' % ([reqStageState.state.pose.position.x, 
        #                                                                 reqStageState.state.pose.position.y]))
        self.ptsToolRefExternal = PointStamped(Header(frame_id=reqStageState.state.header.frame_id),
                                               Point(x=reqStageState.state.pose.position.x,
                                                     y=reqStageState.state.pose.position.y,
                                                     z=reqStageState.state.pose.position.z))
        self.ptsToolRefExternal.point.y *= -1
        try:
            self.tfrx.waitForTransform("Stage", self.ptsToolRefExternal.header.frame_id, rospy.Time(), rospy.Duration(1.0))
            self.ptsToolRef = self.tfrx.transformPoint('Stage', self.ptsToolRefExternal)
            #self.ptsToolRef = self.ptsToolRefExternal
            
        except tf.Exception:
            pass

        if reqStageState.speed is not None:
            self.speedCommandTool = reqStageState.speed # Requested speed for positioning.
        else:
            self.speedCommandTool = self.speedStageMax
        #rospy.logwarn('MotorArm reqStageState.speed=%s' % reqStageState.speed)

        rvStageState = SrvFrameStateResponse()
        rvStageState.state.pose.position.x = reqStageState.state.pose.position.x
        rvStageState.state.pose.position.y = reqStageState.state.pose.position.y
        rvStageState.state.pose.position.z = reqStageState.state.pose.position.z

        return rvStageState
    

    def EndEffectorOffset_callback(self, ptOffset):
        self.ptOffsetSense = ptOffset #Point(0,0,0)#
        
        
    def SignalInput_callback (self, srvSignal):
        #rospy.logwarn ('MotorArm signal pt=%s' % [srvSignal.pts.point.x, srvSignal.pts.point.y])

        rv = SrvSignalResponse()
        rv.success = False
        if self.initialized:
            self.ptsToolRefExternal = srvSignal.pts #self.pattern.points[self.iPoint]
            self.ptsToolRefExternal.point.y *= -1
            try:
                self.tfrx.waitForTransform("Stage", self.ptsToolRefExternal.header.frame_id, rospy.Time(), rospy.Duration(1.0))
                self.ptsToolRef = self.tfrx.transformPoint('Stage', self.ptsToolRefExternal)
                #self.ptsToolRef = self.ptsToolRefExternal
    
                try:
                    self.speedCommandTool = self.speedStageMax
                    rv.success = True
                except AttributeError:
                    pass
                #rospy.logwarn ('MotorArm signal pts=%s' % [self.ptsToolRef.point.x,self.ptsToolRef.point.y])
            except tf.Exception:
                pass
        
        return rv


    # Create a vector with direction of ptDir, and magnitude of ptMag.
    def ScaleVecToMag (self, ptDir, ptMag):
        magPtDir = N.linalg.norm([ptDir.x, ptDir.y, ptDir.z])
        magPtMag = N.linalg.norm([ptMag.x, ptMag.y, ptMag.z])
        
        ptNew = Point (x=magPtMag/magPtDir*ptDir.x,
                       y=magPtMag/magPtDir*ptDir.y,
                       z=magPtMag/magPtDir*ptDir.z)
        return ptDir
    

    def HomeStage_callback(self, reqStageState):
        while not self.initialized:
            rospy.sleep(0.1)
            
        with self.lock:
            try:
                self.Park_joint1()
            except (rospy.ServiceException, IOError), e:
                rospy.logwarn ("MotorArm FAILED %s"%e)
                
        rvStageState = SrvFrameStateResponse()
        rospy.loginfo ('MotorArm HomeStage_callback rvStageState=%s' % rvStageState)
        return rvStageState
        
        
    def Calibrate_callback(self, req):
        # Integer values for directions - used in usb set/get
        POSITIVE = 0
        NEGATIVE = 1
        
        # Convert parking coordinates to angles.
        self.xPark = 0.0
        self.yPark = 0.0
        with self.lock:
            q1park = self.GetThetaFromXy(self.xPark, self.yPark)

        q1park = 0.0
        q1origin = -N.pi/2-0.3 # From the index switch

        rospy.loginfo ('MotorArm Calibrating: q1origin=%s, q1park=%s' % (q1origin, q1park))
        with self.lock:
            rv = self.Calibrate_joint1(NEGATIVE, q1origin, q1park, True) # True=find index switch; False=don't find index switch.
            rospy.loginfo ('MotorArm Calibrated joint1')
            q1index = rv.position

        rvStageState = self.GetStageState()
        rospy.loginfo ('MotorArm Calibrate_callback rvStageState=%s' % rvStageState)
        return rvStageState
    

    def GetState(self):  
        if self.initialized:
            with self.lock:
                try:
                    self.jointstate1 = self.GetState_joint1()
                except (rospy.ServiceException, IOError), e:
                    rospy.logwarn ("MotorArm FAILED %s"%e)
                    self.jointstate1 = None
                #rospy.logwarn('MotorArm [j1,j2]=%s' % [self.jointstate1.position,self.jointstate2.position])
                    

    def SendTransforms(self):  
        if self.initialized:
            if (self.jointstate1 is not None):                    
                now = rospy.Time.now()
                #rospy.loginfo ('MotorArm self.jointstate1=%s' % self.jointstate1)

                # Publish the joint states (for rviz, etc)    
                self.js.header.seq = self.js.header.seq + 1
                self.js.header.stamp = now
                self.js.position = [self.jointstate1.position]
                self.pubJointState.publish(self.js)
    
                (self.ptEeSense.x, self.ptEeSense.y) = self.GetXyFromTheta(self.jointstate1.position)
                state = MsgFrameState()
                state.header.stamp = now
                state.header.frame_id = 'Stage'
                state.pose.position.x = self.ptEeSense.x
                state.pose.position.y = self.ptEeSense.y
                qEE = tf.transformations.quaternion_from_euler(0.0, 0.0, self.jointstate1.position)
                state.pose.orientation.x = qEE[0]
                state.pose.orientation.y = qEE[1]
                state.pose.orientation.z = qEE[2]
                state.pose.orientation.w = qEE[3]
                self.pubEndEffector.publish (state)
                #rospy.loginfo ('MotorArm publish state=%s' % state)
            
        
        
                # Publish the link transforms.
                
        
                self.tfbx.sendTransform((0.0, 0.0, 0.0), 
                                        tf.transformations.quaternion_from_euler(0.0, 0.0, 0.0),
                                        now,
                                        "link0",     # child
                                        "Stage"      # parent
                                        )

                self.tfbx.sendTransform((0.0, 0.0, 0.0), 
                                        qEE,
                                        now,
                                        "link1",     # child
                                        "link0"      # parent
                                        )
                
                # Frame EndEffector
                self.tfbx.sendTransform((state.pose.position.x, state.pose.position.y, state.pose.position.z), 
                                        qEE,
                                        now,
                                        "EndEffector",     # child
                                        "Stage"      # parent
                                        )
                # Frame Target
                if self.ptsToolRef is not None:
                    markerTarget = Marker(header=Header(stamp=now,
                                                        frame_id=self.ptsToolRef.header.frame_id),
                                          ns='target',
                                          id=0,
                                          type=2, #SPHERE,
                                          action=0,
                                          pose=Pose(position=Point(x=self.ptsToolRef.point.x, 
                                                                   y=self.ptsToolRef.point.y, 
                                                                   z=self.ptsToolRef.point.z)),
                                          scale=Vector3(x=3.0,
                                                        y=3.0,
                                                        z=3.0),
                                          color=ColorRGBA(a=0.5,
                                                          r=1.0,
                                                          g=0.1,
                                                          b=0.1),
                                          lifetime=rospy.Duration(1.0))
                    self.pubMarker.publish(markerTarget)

                    markerToolOffset   = Marker(header=Header(stamp = now,
                                                              frame_id='Stage'),
                                          ns='tooloffset',
                                          id=1,
                                          type=0, #ARROW,
                                          action=0,
                                          scale=Vector3(x=0.1, # Shaft diameter
                                                        y=0.2, # Head diameter
                                                        z=0.0),
                                          color=ColorRGBA(a=0.8,
                                                          r=1.0,
                                                          g=1.0,
                                                          b=1.0),
                                          lifetime=rospy.Duration(1.0),
                                          points=[Point(x=state.pose.position.x, 
                                                        y=state.pose.position.y, 
                                                        z=state.pose.position.z),
                                                  Point(x=state.pose.position.x+self.ptOffsetSense.x, 
                                                        y=state.pose.position.y+self.ptOffsetSense.y, 
                                                        z=state.pose.position.z+self.ptOffsetSense.z)])
                    self.pubMarker.publish(markerToolOffset)



    # SendTargetCommand()
    #   Updates the motor command with the current target.
    #
    def SendTargetCommand(self):
        #rospy.loginfo ('MotorArm ptToolRef=%s' % self.ptToolRef)
        if self.ptsToolRef is not None:
            #self.speedStageMax = rospy.get_param('motorarm/speed_max', 200.0)

            # Compute various vectors.
            self.ptContourSense.x = self.ptEeSense.x + self.ptOffsetSense.x
            self.ptContourSense.y = self.ptEeSense.y + self.ptOffsetSense.y
            self.ptContourError.x = self.ptsToolRef.point.x - self.ptContourSense.x #- self.ptOffsetSense.x
            self.ptContourError.y = self.ptsToolRef.point.y - self.ptContourSense.y #- self.ptOffsetSense.y
            self.ptToolRefError.x = self.ptsToolRef.point.x - self.ptEeSense.x
            self.ptToolRefError.y = self.ptsToolRef.point.y - self.ptEeSense.y

            
            # Get the end-effector ref coordinates.
            # Option A:
            #ptRef = self.ScaleVecToMag(self.ptToolRefError, self.ptOffsetSense)
            #self.ptEeRef.x = self.ptsToolRef.point.x+ptRef.x
            #self.ptEeRef.y = self.ptsToolRef.point.y+ptRef.y

            # Option B: works ok.
            #kTest = rospy.get_param('motorarm/kTest', 0.0)
            #self.ptEeRef.x = self.ptsToolRef.point.x - self.ptOffsetSense.x + kTest*self.ptContourError.x
            #self.ptEeRef.y = self.ptsToolRef.point.y - self.ptOffsetSense.y + kTest*self.ptContourError.y

            # Option C: best so far.
            ptRef = self.ScaleVecToMag(self.ptContourError, self.ptOffsetSense)
            self.ptEeRef.x = self.ptsToolRef.point.x + ptRef.x
            self.ptEeRef.y = self.ptsToolRef.point.y + ptRef.y
            
            
            # PID Gains & Parameters.
            #self.kP = rospy.get_param('motorarm/kP', 1.0)
            #self.kI = rospy.get_param('motorarm/kI', 0.0)
            #self.kD = rospy.get_param('motorarm/kD', 0.0)
            #self.maxI = rospy.get_param('motorarm/maxI', 40.0)
            #self.kWindup = rospy.get_param('motorarm/kWindup', 0.0)

            # PID control of the end-effector error.
            self.ptEeError.x = self.ptEeRef.x - self.ptEeSense.x
            self.ptEeError.y = self.ptEeRef.y - self.ptEeSense.y
            self.ptEeIerror.x = self.ptEeIerror.x + self.ptEeError.x
            self.ptEeIerror.y = self.ptEeIerror.y + self.ptEeError.y
            self.ptEeDerror.x = self.ptEeError.x - self.ptEeErrorPrev.x
            self.ptEeDerror.y = self.ptEeError.y - self.ptEeErrorPrev.y
            ptPID = Point(self.kP*self.ptEeError.x + self.kI*self.ptEeIerror.x + self.kD*self.ptEeDerror.x,
                          self.kP*self.ptEeError.y + self.kI*self.ptEeIerror.y + self.kD*self.ptEeDerror.y,
                          0.0)
            
            # Anti-windup
            self.ptEeIerrorClipped = self.ClipPtMag (self.ptEeIerror, self.maxI)
            self.ptAntiwindup = Point(self.kWindup * (self.ptEeIerror.x - self.ptEeIerrorClipped.x),
                                      self.kWindup * (self.ptEeIerror.y - self.ptEeIerrorClipped.y),
                                      self.kWindup * (self.ptEeIerror.z - self.ptEeIerrorClipped.z))
            magP = N.linalg.norm([self.ptEeError.x, self.ptEeError.y])
            magI = N.linalg.norm([self.ptEeIerror.x, self.ptEeIerror.y])
            magD = N.linalg.norm([self.ptEeDerror.x, self.ptEeDerror.y])
            magPID = N.linalg.norm([ptPID.x, ptPID.y])
            #magPIDRaw = N.linalg.norm([ptPIDRaw.x, ptPIDRaw.y])
            #rospy.logwarn('[P,I,D]=[%0.2f,%0.2f,%0.2f], PID=%0.4f' % (magP,magI,magD, magPID))
            self.ptEeIerror.x -= self.ptAntiwindup.x
            self.ptEeIerror.y -= self.ptAntiwindup.y

            # Get the command for the hardware.            
            self.ptEeCommand.x = ptPID.x + self.ptEeSense.x
            self.ptEeCommand.y = ptPID.y + self.ptEeSense.y
            
            self.ptEeErrorPrev.x = self.ptEeError.x 
            self.ptEeErrorPrev.y = self.ptEeError.y 
            
            
            # Get the command for the hardware.            
            #self.ptEeCommand.x = self.ptsToolRef.point.x
            #self.ptEeCommand.y = self.ptsToolRef.point.y
            
            #rospy.logwarn ('MotorArm ptEeCommand=%s' % [self.ptEeCommand.x, self.ptEeCommand.y])

            #########################
#            markerTest = Marker(header=Header(stamp = rospy.Time.now(),
#                                                frame_id='Plate'),
#                                  ns='ptEeRef',
#                                  id=3,
#                                  type=2, #SPHERE,
#                                  action=0,
#                                  pose=Pose(position=Point(x=self.ptEeRef.x, 
#                                                           y=self.ptEeRef.y, 
#                                                           z=self.ptEeRef.z)),
#                                  scale=Vector3(x=1.0,
#                                                y=1.0,
#                                                z=3.0),
#                                  color=ColorRGBA(a=0.5,
#                                                  r=0.1,
#                                                  g=1.0,
#                                                  b=0.1),
#                                  lifetime=rospy.Duration(1.0))
#            self.pubMarker.publish(markerTest)
#
#            markerTest = Marker(header=Header(stamp = rospy.Time.now(),
#                                    frame_id='Plate'),
#                      ns='ptContourError',
#                      id=4,
#                      type=2, #SPHERE,
#                      action=0,
#                      pose=Pose(position=Point(x=self.ptContourError.x, 
#                                               y=self.ptContourError.y, 
#                                               z=self.ptContourError.z)),
#                      scale=Vector3(x=1.0,
#                                    y=1.0,
#                                    z=3.0),
#                      color=ColorRGBA(a=0.5,
#                                      r=0.0,
#                                      g=1.0,
#                                      b=0.1),
#                      lifetime=rospy.Duration(1.0))
#            self.pubMarker.publish(markerTest)
#            
#            markerTest = Marker(header=Header(stamp = rospy.Time.now(),
#                                    frame_id='Plate'),
#                      ns='ptOffsetSense',
#                      id=5,
#                      type=2, #SPHERE,
#                      action=0,
#                      pose=Pose(position=Point(x=self.ptOffsetSense.x, 
#                                               y=self.ptOffsetSense.y, 
#                                               z=self.ptOffsetSense.z)),
#                      scale=Vector3(x=1.0,
#                                    y=1.0,
#                                    z=3.0),
#                      color=ColorRGBA(a=0.5,
#                                      r=0.1,
#                                      g=1.0,
#                                      b=0.0),
#                      lifetime=rospy.Duration(1.0))
#            self.pubMarker.publish(markerTest)
            #########################
            
            # Display a vector in rviz.
            ptBase = self.ptEeSense
            ptEnd = self.ptEeCommand
            markerCommand= Marker(header=Header(stamp = rospy.Time.now(),
                                                frame_id='Stage'),
                                  ns='command',
                                  id=2,
                                  type=0, #ARROW,
                                  action=0,
                                  scale=Vector3(x=0.1, # Shaft diameter
                                                y=0.2, # Head diameter
                                                z=0.0),
                                  color=ColorRGBA(a=0.9,
                                                  r=0.5,
                                                  g=1.0,
                                                  b=0.5),
                                  lifetime=rospy.Duration(1.0),
                                  points=[ptBase, ptEnd])
            self.pubMarker.publish(markerCommand)

            
            # Get the desired positions for each joint.
            if self.ptsToolRef.header.frame_id=='joint': # Jointspace uses pt.x as the angle
                angleNext = self.ptEeCommand.x
            else:                                        # Other frames of reference use the angle of cartesian (x,y)
                angleNext = self.GetThetaFromXy(self.ptEeCommand.x, self.ptEeCommand.y)

            # Compute deltas for speed calc.
            time = rospy.Time.now()
            self.dAngle = angleNext - self.jointstate1.position
            #self.dTime = self.ptsToolRef.header.stamp - time
            self.dTime = time - self.timePrev
            self.timePrev = time
    
            if (self.jointstate1 is not None):
                speed = N.abs(self.dAngle / 1)#self.dTime.to_sec())
                
                with self.lock:
                    try:
                        self.SetPositionAtVel_joint1(Header(frame_id=self.names[0]), angleNext, speed)
                    except (rospy.ServiceException, IOError), e:
                        rospy.logwarn ("MotorArm FAILED %s"%e)

        
    def OnShutdown_callback(self):
        rospy.logwarn("MotorArm Closed MotorArm device.")
        #self.Calibrate_callback(None)
        

        
    def Mainloop(self):
        self.LoadServices()
        self.Calibrate_callback(None)
        #self.SetZero_joint1(0.0)
        self.initialized = True

        # Process messages forever.
        rosrate = rospy.Rate(100)
        #try:
        while not rospy.is_shutdown():
            #rospy.logwarn('jointstate1=%s' % self.jointstate1)
            self.GetState()
            self.SendTransforms()
            self.SendTargetCommand()
            rosrate.sleep()
                
        #except:
        #    print "Shutting down"
    
    

if __name__ == '__main__':
    try:
        motorarm = MotorArm()
        motorarm.Mainloop()
    except rospy.exceptions.ROSInterruptException: 
        pass
    
    
    

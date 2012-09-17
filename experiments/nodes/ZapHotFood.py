#!/usr/bin/env python
from __future__ import division
import roslib; roslib.load_manifest('experiments')
import rospy
import numpy as N
import ExperimentLib
from geometry_msgs.msg import Point, Twist
from experiments.srv import *
from flycore.msg import MsgFrameState
from galvodirector.msg import MsgGalvoCommand
from patterngen.msg import MsgPattern
from tracking.msg import ArenaState




#######################################################################################################
class ExperimentZapHotFood():
    def __init__(self):
        rospy.init_node('Experiment')
        
        # Fill out the data structure that defines the experiment.
        self.experimentparams = ExperimentParamsRequest()
        
        self.experimentparams.experiment.description = "Food is in the hot zone."
        self.experimentparams.experiment.maxTrials = -1
        self.experimentparams.experiment.trial = 1
        
        self.experimentparams.save.filenamebase = "zaphotfood"
        self.experimentparams.save.arenastate = True
        self.experimentparams.save.video = False
        self.experimentparams.save.bag = False
        self.experimentparams.save.onlyWhileTriggered = False # Saves always.

        self.experimentparams.tracking.exclusionzone.enabled = True
        self.experimentparams.tracking.exclusionzone.point_list = [Point(x=45.0, y=48.0)]
        self.experimentparams.tracking.exclusionzone.radius_list = [8.0]
        
        self.experimentparams.home.enabled = False
        
        self.experimentparams.waitEntry = 0.0
        
        self.experimentparams.triggerEntry.enabled = False
        self.experimentparams.triggerEntry.frameidParent = 'Plate'
        self.experimentparams.triggerEntry.frameidChild = 'Fly1'
        self.experimentparams.triggerEntry.speedAbsParentMin =   0.0
        self.experimentparams.triggerEntry.speedAbsParentMax = 999.0
        self.experimentparams.triggerEntry.speedAbsChildMin  =   0.0
        self.experimentparams.triggerEntry.speedAbsChildMax  = 999.0
        self.experimentparams.triggerEntry.speedRelMin       =   0.0
        self.experimentparams.triggerEntry.speedRelMax       = 999.0
        self.experimentparams.triggerEntry.distanceMin =   0.0
        self.experimentparams.triggerEntry.distanceMax = 999.0
        self.experimentparams.triggerEntry.angleMin =  0.0 * N.pi / 180.0
        self.experimentparams.triggerEntry.angleMax =180.0 * N.pi / 180.0
        self.experimentparams.triggerEntry.angleTest = 'inclusive'
        self.experimentparams.triggerEntry.angleTestBilateral = False
        self.experimentparams.triggerEntry.timeHold = 0.0
        self.experimentparams.triggerEntry.timeout = -1
        
        
        # .move, .lasertrack, and .triggerExit all run concurrently.
        # The first one to finish preempts the others.
        self.experimentparams.move.enabled = False
        
        
        self.experimentparams.lasertrack.enabled = True
        self.experimentparams.lasertrack.pattern_list = []
        self.experimentparams.lasertrack.statefilterHi_list = []
        self.experimentparams.lasertrack.statefilterLo_list = []
        self.experimentparams.lasertrack.statefilterCriteria_list = []
        for iFly in range(rospy.get_param('nFlies', 0)):#range(3):#
            self.experimentparams.lasertrack.pattern_list.append(MsgPattern(mode       = 'byshape',
                                                                            shape      = 'grid',
                                                                            frame_id   = 'Fly%d' % (iFly+1),
                                                                            hzPattern  = 40.0,
                                                                            hzPoint    = 1000.0,
                                                                            count      = 1,
                                                                            size       = Point(x=0,
                                                                                               y=0),
                                                                            preempt    = False,
                                                                            param      = 3), # Peano curve level.
                                                                 )
            #self.experimentparams.lasertrack.statefilterHi_list.append("{'speed':5.0}")
            #self.experimentparams.lasertrack.statefilterLo_list.append("{'speed':0.0}")
            #self.experimentparams.lasertrack.statefilterHi_list.append("{'velocity':{'linear':{'x':+6,'y':+6}}}")
            #self.experimentparams.lasertrack.statefilterLo_list.append("{'velocity':{'linear':{'x':-6,'y':-6}}}")
            #self.experimentparams.lasertrack.statefilterHi_list.append("{'velocity':{'angular':{'z':999}}}")
            #self.experimentparams.lasertrack.statefilterLo_list.append("{'velocity':{'angular':{'z':0.5}}}")
            self.experimentparams.lasertrack.statefilterHi_list.append("{'pose':{'position':{'x':-30, 'y':-30}}}")
            self.experimentparams.lasertrack.statefilterLo_list.append("{'pose':{'position':{'x':-50, 'y':-50}}}")
            self.experimentparams.lasertrack.statefilterCriteria_list.append("exclusive")
        self.experimentparams.lasertrack.timeout = -1
        
        self.experimentparams.triggerExit.enabled = True
        self.experimentparams.triggerExit.frameidParent = 'Plate'
        self.experimentparams.triggerExit.frameidChild = 'Fly1'
        self.experimentparams.triggerExit.speedAbsParentMin =   0.0
        self.experimentparams.triggerExit.speedAbsParentMax = 999.0
        self.experimentparams.triggerExit.speedAbsChildMin  =   0.0
        self.experimentparams.triggerExit.speedAbsChildMax  = 999.0
        self.experimentparams.triggerExit.speedRelMin       =   0.0
        self.experimentparams.triggerExit.speedRelMax       = 999.0
        self.experimentparams.triggerExit.distanceMin = 999.0
        self.experimentparams.triggerExit.distanceMax = 111.0 # i.e. never
        self.experimentparams.triggerExit.angleMin =  0.0000 * N.pi / 180.0
        self.experimentparams.triggerExit.angleMax =359.9999 * N.pi / 180.0
        self.experimentparams.triggerExit.angleTest = 'inclusive'
        self.experimentparams.triggerExit.angleTestBilateral = False
        self.experimentparams.triggerExit.timeHold = 0.0
        self.experimentparams.triggerExit.timeout = 3600

        self.experimentparams.waitExit = 0.0
        
        self.experiment = ExperimentLib.Experiment(self.experimentparams)



    def Run(self):
        self.experiment.Run()
        



if __name__ == '__main__':
    experiment = ExperimentZapHotFood()
    experiment.Run()
        

        

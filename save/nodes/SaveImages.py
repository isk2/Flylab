#!/usr/bin/env python
from __future__ import division
import roslib; roslib.load_manifest('save')
import rospy

import tf
import sys
import time, os, subprocess
import threading
import numpy as N

from sensor_msgs.msg import Image
import cv
from cv_bridge import CvBridge, CvBridgeError

from flycore.msg import MsgFrameState
from experiments.srv import Trigger, ExperimentParams


def Chdir(dir):
    try:
        os.chdir(dir)
    except (OSError):
        os.mkdir(dir)
        os.chdir(dir)


###############################################################################
# Save() is a ROS node.  It saves Image messages from a list of topics to image files (.png, .bmp, etc).
#
#  At the end of each trial, a video is made.  
# There should be one video frame per line in the .csv
#
class SaveImages:
    def __init__(self):
        self.initialized = False
        self.dirWorking_base = os.path.expanduser("~/FlylabData")
        Chdir(self.dirWorking_base)

        # Create new directory each day
        self.dirRelative = time.strftime("%Y_%m_%d")
        self.dirWorking = self.dirWorking_base + "/" + self.dirRelative
        Chdir(self.dirWorking)

        self.fileErrors = open('/dev/null', 'w')

        self.imageext = rospy.get_param('save/imageext', 'png')
        
        self.cvbridge = CvBridge()
        self.lockImage = threading.Lock()
        self.lockVideo = threading.Lock()
        self.filename = None
        self.fid = None
        self.bSaveImages = False
        self.bSaveOnlyWhileTriggered = False # False: Save everything from one trial_start to the trial_end.  True:  Save everything from trigger=on to trigger=off.
        self.bTriggered = False
        #self.imagetopic = rospy.get_param('save/imagetopic', 'camera/image_rect')
        self.save = None

        # All the per-topic stuff.
        self.subImage = {}          # All the subscriptions.
        self.filenameVideo = {}     # The video filename of each imagetopic.
        self.dirFrames = {}         # The directory of each imagetopic.
        self.iFrame = {}            # The frame counter for each imagetopic.
        self.processVideoConversion = {}

        rospy.on_shutdown(self.OnShutdown_callback)
        
        # Offer some services.
        rospy.Service('saveimages/init',            ExperimentParams, self.Init_callback)
        rospy.Service('saveimages/trial_start',     ExperimentParams, self.TrialStart_callback)
        rospy.Service('saveimages/trial_end',       ExperimentParams, self.TrialEnd_callback)
        rospy.Service('saveimages/trigger',         Trigger,          self.Trigger_callback)
        rospy.Service('saveimages/wait_until_done', ExperimentParams, self.WaitUntilDone_callback)
        
        self.initialized = True


    def OnShutdown_callback(self):
        with self.lockImage:
            if (self.fileErrors is not None) and (not self.fileErrors.closed):
                self.fileErrors.close()
                self.fileErrors = None
            
        

    # Service callback to perform initialization that requires experimentparams, e.g. subscribing to image topics.
    def Init_callback(self, experimentparams):
        self.save = experimentparams.save
        
        for imagetopic in self.save.imagetopic_list:
            rospy.loginfo('Subscribing to %s' % imagetopic)
            self.subImage[imagetopic] = rospy.Subscriber(imagetopic, Image, self.Image_callback, callback_args=imagetopic)

        return True



    def WaitUntilDone_callback(self, experimentparams):
        for imagetopic,value in self.processVideoConversion.iteritems():
            self.processVideoConversion[imagetopic].wait()

        return True

            
                    
    # TrialStart_callback()
    # 
    def TrialStart_callback(self, experimentparams):
        self.bSaveImages = False
        while (not self.initialized):
            rospy.sleep(0.5)
            
        self.save = experimentparams.save
        self.bSaveOnlyWhileTriggered = self.save.onlyWhileTriggered
        
        if (self.save.images):                
            # Go to the directory:  dirVideo = 'FlylabData/YYYY_MM_DD'
            self.dirBase = os.path.expanduser("~/FlylabData")
            Chdir(self.dirBase)
            self.dirVideo = self.dirBase + "/" + time.strftime("%Y_%m_%d")
            Chdir(self.dirVideo)
                
            # Initialize vars for each imagetopic.
            # Make a subdir and video filename for each timestamped imagetopic:  dirFrames['image_raw'] = 'test20130418131415_camera_image_raw'
            for (imagetopic,value) in self.subImage.iteritems():
                self.dirFrames[imagetopic] = self.save.filenamebasestamped+'_'+imagetopic.replace('/','_')
                self.filenameVideo[imagetopic] = "%s/%s.mov" % (self.dirVideo, self.dirFrames[imagetopic]) 
                self.iFrame[imagetopic] = 0
    
                try:
                    os.mkdir(self.dirFrames[imagetopic])
                except OSError, e:
                    rospy.logwarn ('Cannot create directory %s: %s' % (self.dirFrames[imagetopic],e))
        
                
        if (self.save.images) and ((self.bSaveOnlyWhileTriggered and self.bTriggered) or (not self.bSaveOnlyWhileTriggered)):
            self.bSaveImages = True
        else:
            self.bSaveImages = False
            

            
        return True
                
                
    # Trigger_callback() 
    #    Set the trigger state, and detect edges.
    #
    def Trigger_callback(self, reqTrigger):
        self.bSaveImages = False
        while (not self.initialized):
            rospy.sleep(0.5)

        bRisingEdge = False
        bFallingEdge = False
        if self.bTriggered != reqTrigger.triggered:
            self.bTriggered = reqTrigger.triggered
            if self.bTriggered: # Rising edge.
                bRisingEdge = True
            else:
                bFallingEdge = True


        if (self.save.images) and ((self.bSaveOnlyWhileTriggered and self.bTriggered) or (not self.bSaveOnlyWhileTriggered)):
            self.bSaveImages = True
        else:
            self.bSaveImages = False
            
        
        return self.bTriggered
        

    # TrialEnd_callback()
    # 
    def TrialEnd_callback(self, experimentparams):
        self.bSaveImages = False
        while (not self.initialized):
            rospy.sleep(0.5)

        if (self.save.images):
            # If there are frame files to convert, then convert them.
            for (imagetopic,filenameVideo) in self.filenameVideo.iteritems():
                self.WriteVideoFromFrames(filenameVideo, imagetopic)
                self.iFrame[imagetopic] = 0
                
            self.filenameVideo = {}
                
                
        return True
                
                
    def Image_callback(self, image, imagetopic):
        if (self.initialized) and (self.bSaveImages) and (image is not None):
            with self.lockImage:
                # Convert ROS image to OpenCV image
                try:
                  cv_image = cv.GetImage(self.cvbridge.imgmsg_to_cv(image, "passthrough"))
                except CvBridgeError, e:
                  print e
                # cv.CvtColor(cv_image, self.im_display, cv.CV_GRAY2RGB)
    
                self.WriteImageFile(cv_image, imagetopic)

        
    def get_imagenames(self, dir):
        proc_ls = subprocess.Popen('ls %s/*.%s' % (dir, self.imageext),
                                    shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=self.fileErrors)
        out = proc_ls.stdout.readlines()
        imagenames = [s.rstrip() for s in out]
        return imagenames
    

    def DeleteFrameFiles(self):
        #try:
        #    rospy.logwarn('Deleting frame files.')
        #    subprocess.call('rm '+self.dirFrames+'/*.png', shell=True)
        #except OSError:
        #    pass
        pass
        


    def WriteImageFile(self, cvimage, imagetopic):
        filenameImage = self.dirFrames[imagetopic]+"/{num:06d}.{ext:s}".format(num=self.iFrame[imagetopic], ext=self.imageext)

        cv.SaveImage(filenameImage, cvimage)
        self.iFrame[imagetopic] += 1


    def WriteVideoFromFrames(self, filenameVideo, imagetopic):
        with self.lockVideo:
            cmdCreateVideoFile = 'avconv -r 60 -i %s/%%06d.%s -r 60 %s' % (self.dirFrames[imagetopic], self.imageext, filenameVideo)
            rospy.logwarn('Converting images to video using command:')
            rospy.logwarn (cmdCreateVideoFile)
            try:
                self.processVideoConversion[imagetopic] = subprocess.Popen(cmdCreateVideoFile, shell=True)
            except:
                rospy.logerr('Exception running avconv')
                



    def Main(self):
        rospy.spin()
        

if __name__ == '__main__':
    rospy.init_node('Save', log_level=rospy.INFO)
    saveimages = SaveImages()
    saveimages.Main()
    

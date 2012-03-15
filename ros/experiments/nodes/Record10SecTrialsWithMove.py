#!/usr/bin/env python
from __future__ import division
import roslib; roslib.load_manifest('experiments')
import rospy
import numpy as N
import ExperimentLib
from experiments.srv import *



#######################################################################################################
class ExperimentRecord10SecTrialsWithMove():
    def __init__(self):
        rospy.init_node('Experiment')
        
        # Fill out the data structure that defines the experiment.
        self.experimentparams = ExperimentParamsRequest()
        
        self.experimentparams.experiment.description = "Record 10 Second Trials With Robot Move"
        self.experimentparams.experiment.maxTrials = -1
        self.experimentparams.experiment.trial = 1
        
        self.experimentparams.save.filenamebase = "tensec"
        self.experimentparams.save.arenastate = True
        self.experimentparams.save.video = False
        self.experimentparams.save.bag = False
        self.experimentparams.save.onlyWhileTriggered = True
        
        self.experimentparams.home.enabled = True
        self.experimentparams.home.x = 0.0
        self.experimentparams.home.y = 0.0
        self.experimentparams.home.timeout = -1
        self.experimentparams.home.tolerance = 2
        
        self.experimentparams.waitEntry = 0.0
        
        self.experimentparams.triggerEntry.enabled = False
        self.experimentparams.triggerEntry.distanceMin =   0.0
        self.experimentparams.triggerEntry.distanceMax = 999.0
        self.experimentparams.triggerEntry.speedMin =   0.0
        self.experimentparams.triggerEntry.speedMax = 999.0
        self.experimentparams.triggerEntry.angleMin =  0.0 * N.pi / 180.0
        self.experimentparams.triggerEntry.angleMax =180.0 * N.pi / 180.0
        self.experimentparams.triggerEntry.angleTest = 'inclusive'
        self.experimentparams.triggerEntry.angleTestBilateral = True
        self.experimentparams.triggerEntry.timeHold = 0.0
        self.experimentparams.triggerEntry.timeout = -1
        
        self.experimentparams.move.enabled = True
        self.experimentparams.move.tracking = True
        self.experimentparams.move.frameidOriginPosition = "Plate"
        self.experimentparams.move.frameidOriginAngle = "Plate"
        self.experimentparams.move.distance = 50
        self.experimentparams.move.angle =  0.0 * N.pi / 180.0
        self.experimentparams.move.angleType = 'random'
        self.experimentparams.move.speed = 100
        self.experimentparams.move.speedType = 'constant'
        #self.experimentparams.move.trajectoryType = 'linearparabolic' #'cubic' 'quintic' 
        self.experimentparams.move.tolerance = 2
        self.experimentparams.move.timeout = -1
        
        self.experimentparams.triggerExit.enabled = True
        self.experimentparams.triggerExit.distanceMin = 999.0
        self.experimentparams.triggerExit.distanceMax =   0.0
        self.experimentparams.triggerExit.speedMin = 999.0
        self.experimentparams.triggerExit.speedMax = 999.0
        self.experimentparams.triggerExit.angleMin =  0.0 * N.pi / 180.0
        self.experimentparams.triggerExit.angleMax =180.0 * N.pi / 180.0
        self.experimentparams.triggerExit.angleTest = 'inclusive'
        self.experimentparams.triggerExit.angleTestBilateral = True
        self.experimentparams.triggerExit.timeHold = 0.0
        self.experimentparams.triggerExit.timeout = 0

        self.experiment = ExperimentLib.Experiment(self.experimentparams)


    def Run(self):
        self.experiment.Run()


if __name__ == '__main__':
    try:
        experiment = ExperimentRecord10SecTrialsWithMove()
        experiment.Run()
        
    except KeyboardInterrupt:
        rospy.loginfo("Shutting down")

        

#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of the Willow Garage nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import roslib
roslib.load_manifest('flysim_tf')
import rospy

import math
import tf
import flysim.msg
import flysim.srv

if __name__ == '__main__':
    rospy.init_node('tf_flysim')

    tfrx = tf.TransformListener()

    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', flysim.srv.Spawn)
    spawner(4, 2, 0, 'fly')

    robot_vel = rospy.Publisher('robot/command_velocity', flysim.msg.Velocity)

    rate = rospy.Rate(10.0)
    dist_max = 40
    dist_min = 4
    while not rospy.is_shutdown():
        try:
            (trans,rot) = tfrx.lookupTransform('/robot', '/fly', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException):
            continue

        # angular = 4 * math.atan2(trans[1], trans[0])
        # linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)

        # Add distance bounds
        dist = math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        angular = 4 * math.atan2(trans[1], trans[0])
        if (dist_min < dist) and (dist < dist_max):
            linear = 1.0 * dist
        else:
            linear = 0
        robot_vel.publish(flysim.msg.Velocity(linear, angular))

        rate.sleep()

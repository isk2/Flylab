## *********************************************************
## 
## File autogenerated for the camera1394v2 package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

##**********************************************************
## Software License Agreement (BSD License)
##
##  Copyright (c) 2008, Willow Garage, Inc.
##  All rights reserved.
##
##  Redistribution and use in source and binary forms, with or without
##  modification, are permitted provided that the following conditions
##  are met:
##
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above
##     copyright notice, this list of conditions and the following
##     disclaimer in the documentation and/or other materials provided
##     with the distribution.
##   * Neither the name of the Willow Garage nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
##  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
##  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
##  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
##  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
##  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
##  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
##  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
##  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
##  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
##  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
##  POSSIBILITY OF SUCH DAMAGE.
##**********************************************************/

config_description = [{'srcline': 50, 'description': 'Global Unique ID of camera, 16 hex digits (use first camera if null).', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'guid', 'edit_method': '', 'default': '', 'level': 3, 'min': '', 'type': 'str'}, {'srcline': 81, 'description': 'IIDC video mode.', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'video_mode', 'edit_method': "{'enum_description': 'Video mode for camera.', 'enum': [{'srcline': 53, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '160x120_yuv444', 'ctype': 'std::string', 'type': 'str', 'name': 'Format0_Mode0'}, {'srcline': 54, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '320x240_yuv422', 'ctype': 'std::string', 'type': 'str', 'name': 'Format0_Mode1'}, {'srcline': 55, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '640x480_yuv411', 'ctype': 'std::string', 'type': 'str', 'name': 'Format0_Mode2'}, {'srcline': 56, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '640x480_yuv422', 'ctype': 'std::string', 'type': 'str', 'name': 'Format0_Mode3'}, {'srcline': 57, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '640x480_rgb8', 'ctype': 'std::string', 'type': 'str', 'name': 'Format0_Mode4'}, {'srcline': 58, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '640x480_mono8', 'ctype': 'std::string', 'type': 'str', 'name': 'Format0_Mode5'}, {'srcline': 60, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '800x600_yuv422', 'ctype': 'std::string', 'type': 'str', 'name': 'Format1_Mode0'}, {'srcline': 61, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '800x600_rgb8', 'ctype': 'std::string', 'type': 'str', 'name': 'Format1_Mode1'}, {'srcline': 62, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '800x600_mono8', 'ctype': 'std::string', 'type': 'str', 'name': 'Format1_Mode2'}, {'srcline': 64, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '1024x768_yuv422', 'ctype': 'std::string', 'type': 'str', 'name': 'Format1_Mode3'}, {'srcline': 65, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '1024x768_rgb8', 'ctype': 'std::string', 'type': 'str', 'name': 'Format1_Mode4'}, {'srcline': 66, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '1024x768_mono8', 'ctype': 'std::string', 'type': 'str', 'name': 'Format1_Mode5'}, {'srcline': 68, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '1280x960_yuv422', 'ctype': 'std::string', 'type': 'str', 'name': 'Format2_Mode0'}, {'srcline': 69, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '1280x960_rgb8', 'ctype': 'std::string', 'type': 'str', 'name': 'Format2_Mode1'}, {'srcline': 70, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '1280x960_mono8', 'ctype': 'std::string', 'type': 'str', 'name': 'Format2_Mode2'}, {'srcline': 72, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '1600x1200_yuv422', 'ctype': 'std::string', 'type': 'str', 'name': 'Format2_Mode3'}, {'srcline': 73, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '1600x1200_rgb8', 'ctype': 'std::string', 'type': 'str', 'name': 'Format2_Mode4'}, {'srcline': 74, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '1600x1200_mono8', 'ctype': 'std::string', 'type': 'str', 'name': 'Format2_Mode5'}, {'srcline': 76, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': 'format7_mode0', 'ctype': 'std::string', 'type': 'str', 'name': 'Format7_Mode0'}]}", 'default': '640x480_mono8', 'level': 3, 'min': '', 'type': 'str'}, {'srcline': 85, 'description': 'ROS tf frame of reference, resolved with tf_prefix unless absolute.', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'frame_id', 'edit_method': '', 'default': 'camera', 'level': 3, 'min': '', 'type': 'str'}, {'srcline': 88, 'description': 'Camera speed (frames per second).', 'max': 240.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'frame_rate', 'edit_method': '', 'default': 15.0, 'level': 3, 'min': 1.875, 'type': 'double'}, {'srcline': 91, 'description': 'Total IEEE 1394 bus bandwidth (Megabits/second).', 'max': 3200, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'iso_speed', 'edit_method': '', 'default': 400, 'level': 3, 'min': 100, 'type': 'int'}, {'srcline': 95, 'description': 'Camera calibration URL for this video_mode (uncalibrated if null).', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'camera_info_url', 'edit_method': '', 'default': '', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 107, 'description': 'Bayer color encoding pattern (default: none).', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'bayer_pattern', 'edit_method': "{'enum_description': 'Bayer color encoding patterns', 'enum': [{'srcline': 98, 'description': 'No Bayer encoding', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '', 'ctype': 'std::string', 'type': 'str', 'name': 'none'}, {'srcline': 99, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': 'rggb', 'ctype': 'std::string', 'type': 'str', 'name': 'rggb'}, {'srcline': 100, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': 'gbrg', 'ctype': 'std::string', 'type': 'str', 'name': 'gbrg'}, {'srcline': 101, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': 'grbg', 'ctype': 'std::string', 'type': 'str', 'name': 'grbg'}, {'srcline': 102, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': 'bggr', 'ctype': 'std::string', 'type': 'str', 'name': 'bggr'}]}", 'default': '', 'level': 3, 'min': '', 'type': 'str'}, {'srcline': 122, 'description': 'Bayer decoding method (default: ROS image_proc).', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'bayer_method', 'edit_method': "{'enum_description': 'Bayer method', 'enum': [{'srcline': 110, 'description': 'Decode via ROS image_proc', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': '', 'ctype': 'std::string', 'type': 'str', 'name': 'image_proc'}, {'srcline': 111, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': 'DownSample', 'ctype': 'std::string', 'type': 'str', 'name': 'DownSample'}, {'srcline': 112, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': 'Simple', 'ctype': 'std::string', 'type': 'str', 'name': 'Simple'}, {'srcline': 114, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': 'Bilinear', 'ctype': 'std::string', 'type': 'str', 'name': 'Bilinear'}, {'srcline': 115, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': 'HQ', 'ctype': 'std::string', 'type': 'str', 'name': 'HQ'}, {'srcline': 116, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': 'VNG', 'ctype': 'std::string', 'type': 'str', 'name': 'VNG'}, {'srcline': 117, 'description': '', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const char * const', 'value': 'AHD', 'ctype': 'std::string', 'type': 'str', 'name': 'AHD'}]}", 'default': '', 'level': 3, 'min': '', 'type': 'str'}, {'srcline': 134, 'description': 'Brightness control state.', 'max': 4, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'auto_brightness', 'edit_method': "{'enum_description': 'Feature control states', 'enum': [{'srcline': 125, 'description': 'Use fixed value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Off'}, {'srcline': 126, 'description': 'Query current values', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Query'}, {'srcline': 127, 'description': 'Camera sets continuously', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Auto'}, {'srcline': 128, 'description': 'Use explicit value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'Manual'}, {'srcline': 129, 'description': 'Camera sets once', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'OnePush'}, {'srcline': 130, 'description': 'Feature not available', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'None'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 137, 'description': 'Black level offset.', 'max': 4095.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'brightness', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 141, 'description': 'Combined Gain, Iris & Shutter control.', 'max': 4, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'auto_exposure', 'edit_method': "{'enum_description': 'Feature control states', 'enum': [{'srcline': 125, 'description': 'Use fixed value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Off'}, {'srcline': 126, 'description': 'Query current values', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Query'}, {'srcline': 127, 'description': 'Camera sets continuously', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Auto'}, {'srcline': 128, 'description': 'Use explicit value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'Manual'}, {'srcline': 129, 'description': 'Camera sets once', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'OnePush'}, {'srcline': 130, 'description': 'Feature not available', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'None'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 144, 'description': 'Auto exposure value (like contrast).', 'max': 4095.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'exposure', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -10.0, 'type': 'double'}, {'srcline': 147, 'description': 'Gain control state.', 'max': 4, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'auto_gain', 'edit_method': "{'enum_description': 'Feature control states', 'enum': [{'srcline': 125, 'description': 'Use fixed value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Off'}, {'srcline': 126, 'description': 'Query current values', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Query'}, {'srcline': 127, 'description': 'Camera sets continuously', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Auto'}, {'srcline': 128, 'description': 'Use explicit value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'Manual'}, {'srcline': 129, 'description': 'Camera sets once', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'OnePush'}, {'srcline': 130, 'description': 'Feature not available', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'None'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 150, 'description': 'Relative circuit gain.', 'max': 4095.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'gain', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -10.0, 'type': 'double'}, {'srcline': 153, 'description': 'Gamma control state.', 'max': 4, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'auto_gamma', 'edit_method': "{'enum_description': 'Feature control states', 'enum': [{'srcline': 125, 'description': 'Use fixed value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Off'}, {'srcline': 126, 'description': 'Query current values', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Query'}, {'srcline': 127, 'description': 'Camera sets continuously', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Auto'}, {'srcline': 128, 'description': 'Use explicit value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'Manual'}, {'srcline': 129, 'description': 'Camera sets once', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'OnePush'}, {'srcline': 130, 'description': 'Feature not available', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'None'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 156, 'description': 'Gamma expansion exponent.', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'gamma', 'edit_method': '', 'default': 2.2000000000000002, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 159, 'description': 'Hue control state.', 'max': 4, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'auto_hue', 'edit_method': "{'enum_description': 'Feature control states', 'enum': [{'srcline': 125, 'description': 'Use fixed value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Off'}, {'srcline': 126, 'description': 'Query current values', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Query'}, {'srcline': 127, 'description': 'Camera sets continuously', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Auto'}, {'srcline': 128, 'description': 'Use explicit value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'Manual'}, {'srcline': 129, 'description': 'Camera sets once', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'OnePush'}, {'srcline': 130, 'description': 'Feature not available', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'None'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 162, 'description': 'Color phase.', 'max': 4095.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'hue', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 165, 'description': 'Iris control state.', 'max': 4, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'auto_iris', 'edit_method': "{'enum_description': 'Feature control states', 'enum': [{'srcline': 125, 'description': 'Use fixed value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Off'}, {'srcline': 126, 'description': 'Query current values', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Query'}, {'srcline': 127, 'description': 'Camera sets continuously', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Auto'}, {'srcline': 128, 'description': 'Use explicit value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'Manual'}, {'srcline': 129, 'description': 'Camera sets once', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'OnePush'}, {'srcline': 130, 'description': 'Feature not available', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'None'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 168, 'description': 'Iris control.', 'max': 4095.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'iris', 'edit_method': '', 'default': 8.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 171, 'description': 'Saturation control state.', 'max': 4, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'auto_saturation', 'edit_method': "{'enum_description': 'Feature control states', 'enum': [{'srcline': 125, 'description': 'Use fixed value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Off'}, {'srcline': 126, 'description': 'Query current values', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Query'}, {'srcline': 127, 'description': 'Camera sets continuously', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Auto'}, {'srcline': 128, 'description': 'Use explicit value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'Manual'}, {'srcline': 129, 'description': 'Camera sets once', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'OnePush'}, {'srcline': 130, 'description': 'Feature not available', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'None'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 174, 'description': 'Color saturation.', 'max': 4095.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'saturation', 'edit_method': '', 'default': 1.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 177, 'description': 'Sharpness control state.', 'max': 4, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'auto_sharpness', 'edit_method': "{'enum_description': 'Feature control states', 'enum': [{'srcline': 125, 'description': 'Use fixed value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Off'}, {'srcline': 126, 'description': 'Query current values', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Query'}, {'srcline': 127, 'description': 'Camera sets continuously', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Auto'}, {'srcline': 128, 'description': 'Use explicit value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'Manual'}, {'srcline': 129, 'description': 'Camera sets once', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'OnePush'}, {'srcline': 130, 'description': 'Feature not available', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'None'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 180, 'description': 'Image sharpness.', 'max': 4095.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'sharpness', 'edit_method': '', 'default': 1.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 183, 'description': 'Shutter control state.', 'max': 4, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'auto_shutter', 'edit_method': "{'enum_description': 'Feature control states', 'enum': [{'srcline': 125, 'description': 'Use fixed value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Off'}, {'srcline': 126, 'description': 'Query current values', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Query'}, {'srcline': 127, 'description': 'Camera sets continuously', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Auto'}, {'srcline': 128, 'description': 'Use explicit value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'Manual'}, {'srcline': 129, 'description': 'Camera sets once', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'OnePush'}, {'srcline': 130, 'description': 'Feature not available', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'None'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 186, 'description': 'Shutter speed.', 'max': 4095.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'shutter', 'edit_method': '', 'default': 1.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 189, 'description': 'White balance control state.', 'max': 4, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'auto_white_balance', 'edit_method': "{'enum_description': 'Feature control states', 'enum': [{'srcline': 125, 'description': 'Use fixed value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Off'}, {'srcline': 126, 'description': 'Query current values', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Query'}, {'srcline': 127, 'description': 'Camera sets continuously', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Auto'}, {'srcline': 128, 'description': 'Use explicit value', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'Manual'}, {'srcline': 129, 'description': 'Camera sets once', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'OnePush'}, {'srcline': 130, 'description': 'Feature not available', 'srcfile': '../cfg/camera1394v2.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'None'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 193, 'description': 'Blue or U component of white balance.', 'max': 4095.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'white_balance_BU', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 197, 'description': 'Red or V component of white balance.', 'max': 4095.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '../cfg/camera1394v2.cfg', 'name': 'white_balance_RV', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}]

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

for param in config_description:
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

Camera1394v2_Format0_Mode0 = '160x120_yuv444'
Camera1394v2_Format0_Mode1 = '320x240_yuv422'
Camera1394v2_Format0_Mode2 = '640x480_yuv411'
Camera1394v2_Format0_Mode3 = '640x480_yuv422'
Camera1394v2_Format0_Mode4 = '640x480_rgb8'
Camera1394v2_Format0_Mode5 = '640x480_mono8'
Camera1394v2_Format1_Mode0 = '800x600_yuv422'
Camera1394v2_Format1_Mode1 = '800x600_rgb8'
Camera1394v2_Format1_Mode2 = '800x600_mono8'
Camera1394v2_Format1_Mode3 = '1024x768_yuv422'
Camera1394v2_Format1_Mode4 = '1024x768_rgb8'
Camera1394v2_Format1_Mode5 = '1024x768_mono8'
Camera1394v2_Format2_Mode0 = '1280x960_yuv422'
Camera1394v2_Format2_Mode1 = '1280x960_rgb8'
Camera1394v2_Format2_Mode2 = '1280x960_mono8'
Camera1394v2_Format2_Mode3 = '1600x1200_yuv422'
Camera1394v2_Format2_Mode4 = '1600x1200_rgb8'
Camera1394v2_Format2_Mode5 = '1600x1200_mono8'
Camera1394v2_Format7_Mode0 = 'format7_mode0'
Camera1394v2_none = ''
Camera1394v2_rggb = 'rggb'
Camera1394v2_gbrg = 'gbrg'
Camera1394v2_grbg = 'grbg'
Camera1394v2_bggr = 'bggr'
Camera1394v2_image_proc = ''
Camera1394v2_DownSample = 'DownSample'
Camera1394v2_Simple = 'Simple'
Camera1394v2_Bilinear = 'Bilinear'
Camera1394v2_HQ = 'HQ'
Camera1394v2_VNG = 'VNG'
Camera1394v2_AHD = 'AHD'
Camera1394v2_Off = 0
Camera1394v2_Query = 1
Camera1394v2_Auto = 2
Camera1394v2_Manual = 3
Camera1394v2_OnePush = 4
Camera1394v2_None = 5
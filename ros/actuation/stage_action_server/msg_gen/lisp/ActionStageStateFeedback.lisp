; Auto-generated. Do not edit!


(cl:in-package stage_action_server-msg)


;//! \htmlinclude ActionStageStateFeedback.msg.html

(cl:defclass <ActionStageStateFeedback> (roslisp-msg-protocol:ros-message)
  ((state
    :reader state
    :initarg :state
    :type flycore-msg:MsgFrameState
    :initform (cl:make-instance 'flycore-msg:MsgFrameState)))
)

(cl:defclass ActionStageStateFeedback (<ActionStageStateFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ActionStageStateFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ActionStageStateFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name stage_action_server-msg:<ActionStageStateFeedback> is deprecated: use stage_action_server-msg:ActionStageStateFeedback instead.")))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <ActionStageStateFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader stage_action_server-msg:state-val is deprecated.  Use stage_action_server-msg:state instead.")
  (state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ActionStageStateFeedback>) ostream)
  "Serializes a message object of type '<ActionStageStateFeedback>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'state) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ActionStageStateFeedback>) istream)
  "Deserializes a message object of type '<ActionStageStateFeedback>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'state) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ActionStageStateFeedback>)))
  "Returns string type for a message object of type '<ActionStageStateFeedback>"
  "stage_action_server/ActionStageStateFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActionStageStateFeedback)))
  "Returns string type for a message object of type 'ActionStageStateFeedback"
  "stage_action_server/ActionStageStateFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ActionStageStateFeedback>)))
  "Returns md5sum for a message object of type '<ActionStageStateFeedback>"
  "1977707d7eabf7e0ca765b9e57161cd5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ActionStageStateFeedback)))
  "Returns md5sum for a message object of type 'ActionStageStateFeedback"
  "1977707d7eabf7e0ca765b9e57161cd5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ActionStageStateFeedback>)))
  "Returns full string definition for message of type '<ActionStageStateFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%flycore/MsgFrameState state~%~%~%================================================================================~%MSG: flycore/MsgFrameState~%Header header~%geometry_msgs/Pose pose~%geometry_msgs/Twist velocity~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into it's linear and angular parts. ~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ActionStageStateFeedback)))
  "Returns full string definition for message of type 'ActionStageStateFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%flycore/MsgFrameState state~%~%~%================================================================================~%MSG: flycore/MsgFrameState~%Header header~%geometry_msgs/Pose pose~%geometry_msgs/Twist velocity~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into it's linear and angular parts. ~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ActionStageStateFeedback>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'state))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ActionStageStateFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'ActionStageStateFeedback
    (cl:cons ':state (state msg))
))

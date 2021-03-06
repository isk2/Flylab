"""autogenerated by genpy from experiment_msgs/PostSettings.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import experiment_msgs.msg

class PostSettings(genpy.Message):
  _md5sum = "48a755a13f3d22b7d0eaad2bbd55fcd4"
  _type = "experiment_msgs/PostSettings"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """TriggerSettings 	       trigger
float64 			       wait



================================================================================
MSG: experiment_msgs/TriggerSettings
bool 		enabled
string 		frameidParent 	# 'Plate', 'Robot', 'Fly1', 'Fly2' etc
string 		frameidChild 	
float64 	speedAbsParentMin  # Absolute speed of parent frame.
float64 	speedAbsParentMax
float64 	speedAbsChildMin   # Absolute speed of child frame.
float64 	speedAbsChildMax
float64 	speedRelMin  	# Relative speed between frames.
float64 	speedRelMax
float64 	distanceMin     # Distance from parent to child.
float64 	distanceMax
float64 	angleMin		# Angle to child in parent frame.
float64 	angleMax
string  	angleTest		# 'inclusive' or 'exclusive'
bool    	angleTestBilateral
float64 	timeHold
float64 	timeout



"""
  __slots__ = ['trigger','wait']
  _slot_types = ['experiment_msgs/TriggerSettings','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       trigger,wait

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PostSettings, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.trigger is None:
        self.trigger = experiment_msgs.msg.TriggerSettings()
      if self.wait is None:
        self.wait = 0.
    else:
      self.trigger = experiment_msgs.msg.TriggerSettings()
      self.wait = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_struct_B.pack(self.trigger.enabled))
      _x = self.trigger.frameidParent
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.trigger.frameidChild
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_10d.pack(_x.trigger.speedAbsParentMin, _x.trigger.speedAbsParentMax, _x.trigger.speedAbsChildMin, _x.trigger.speedAbsChildMax, _x.trigger.speedRelMin, _x.trigger.speedRelMax, _x.trigger.distanceMin, _x.trigger.distanceMax, _x.trigger.angleMin, _x.trigger.angleMax))
      _x = self.trigger.angleTest
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B3d.pack(_x.trigger.angleTestBilateral, _x.trigger.timeHold, _x.trigger.timeout, _x.wait))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.trigger is None:
        self.trigger = experiment_msgs.msg.TriggerSettings()
      end = 0
      start = end
      end += 1
      (self.trigger.enabled,) = _struct_B.unpack(str[start:end])
      self.trigger.enabled = bool(self.trigger.enabled)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.trigger.frameidParent = str[start:end].decode('utf-8')
      else:
        self.trigger.frameidParent = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.trigger.frameidChild = str[start:end].decode('utf-8')
      else:
        self.trigger.frameidChild = str[start:end]
      _x = self
      start = end
      end += 80
      (_x.trigger.speedAbsParentMin, _x.trigger.speedAbsParentMax, _x.trigger.speedAbsChildMin, _x.trigger.speedAbsChildMax, _x.trigger.speedRelMin, _x.trigger.speedRelMax, _x.trigger.distanceMin, _x.trigger.distanceMax, _x.trigger.angleMin, _x.trigger.angleMax,) = _struct_10d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.trigger.angleTest = str[start:end].decode('utf-8')
      else:
        self.trigger.angleTest = str[start:end]
      _x = self
      start = end
      end += 25
      (_x.trigger.angleTestBilateral, _x.trigger.timeHold, _x.trigger.timeout, _x.wait,) = _struct_B3d.unpack(str[start:end])
      self.trigger.angleTestBilateral = bool(self.trigger.angleTestBilateral)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_struct_B.pack(self.trigger.enabled))
      _x = self.trigger.frameidParent
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.trigger.frameidChild
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_10d.pack(_x.trigger.speedAbsParentMin, _x.trigger.speedAbsParentMax, _x.trigger.speedAbsChildMin, _x.trigger.speedAbsChildMax, _x.trigger.speedRelMin, _x.trigger.speedRelMax, _x.trigger.distanceMin, _x.trigger.distanceMax, _x.trigger.angleMin, _x.trigger.angleMax))
      _x = self.trigger.angleTest
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B3d.pack(_x.trigger.angleTestBilateral, _x.trigger.timeHold, _x.trigger.timeout, _x.wait))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.trigger is None:
        self.trigger = experiment_msgs.msg.TriggerSettings()
      end = 0
      start = end
      end += 1
      (self.trigger.enabled,) = _struct_B.unpack(str[start:end])
      self.trigger.enabled = bool(self.trigger.enabled)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.trigger.frameidParent = str[start:end].decode('utf-8')
      else:
        self.trigger.frameidParent = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.trigger.frameidChild = str[start:end].decode('utf-8')
      else:
        self.trigger.frameidChild = str[start:end]
      _x = self
      start = end
      end += 80
      (_x.trigger.speedAbsParentMin, _x.trigger.speedAbsParentMax, _x.trigger.speedAbsChildMin, _x.trigger.speedAbsChildMax, _x.trigger.speedRelMin, _x.trigger.speedRelMax, _x.trigger.distanceMin, _x.trigger.distanceMax, _x.trigger.angleMin, _x.trigger.angleMax,) = _struct_10d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.trigger.angleTest = str[start:end].decode('utf-8')
      else:
        self.trigger.angleTest = str[start:end]
      _x = self
      start = end
      end += 25
      (_x.trigger.angleTestBilateral, _x.trigger.timeHold, _x.trigger.timeout, _x.wait,) = _struct_B3d.unpack(str[start:end])
      self.trigger.angleTestBilateral = bool(self.trigger.angleTestBilateral)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B3d = struct.Struct("<B3d")
_struct_B = struct.Struct("<B")
_struct_10d = struct.Struct("<10d")

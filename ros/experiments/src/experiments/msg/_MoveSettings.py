"""autogenerated by genmsg_py from MoveSettings.msg. Do not edit."""
import roslib.message
import struct

import experiments.msg

class MoveSettings(roslib.message.Message):
  _md5sum = "1134374486ede5b193275bb436ea75fd"
  _type = "experiments/MoveSettings"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool enabled
string mode  # 'pattern' or 'relative'
MoveRelative relative
MovePattern pattern
float64 timeout


================================================================================
MSG: experiments/MoveRelative
bool tracking
string frameidOriginPosition # 'Plate' or 'Robot' or 'Fly'
string frameidOriginAngle # 'Plate' or 'Robot' or 'Fly'
float64 distance
float64 angle
string angleType # 'random' or 'constant'
float64 speed
string speedType # 'random' or 'constant'
float64 tolerance


================================================================================
MSG: experiments/MovePattern
string shape  # 'constant' or 'circle' or 'square' or 'flylogo' or 'spiral'
float64 hz
int32 count  # -1 means forever
float64 radius


"""
  __slots__ = ['enabled','mode','relative','pattern','timeout']
  _slot_types = ['bool','string','experiments/MoveRelative','experiments/MovePattern','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       enabled,mode,relative,pattern,timeout
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(MoveSettings, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.enabled is None:
        self.enabled = False
      if self.mode is None:
        self.mode = ''
      if self.relative is None:
        self.relative = experiments.msg.MoveRelative()
      if self.pattern is None:
        self.pattern = experiments.msg.MovePattern()
      if self.timeout is None:
        self.timeout = 0.
    else:
      self.enabled = False
      self.mode = ''
      self.relative = experiments.msg.MoveRelative()
      self.pattern = experiments.msg.MovePattern()
      self.timeout = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      buff.write(_struct_B.pack(self.enabled))
      _x = self.mode
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.relative.tracking))
      _x = self.relative.frameidOriginPosition
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.relative.frameidOriginAngle
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2d.pack(_x.relative.distance, _x.relative.angle))
      _x = self.relative.angleType
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_d.pack(self.relative.speed))
      _x = self.relative.speedType
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_d.pack(self.relative.tolerance))
      _x = self.pattern.shape
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_di2d.pack(_x.pattern.hz, _x.pattern.count, _x.pattern.radius, _x.timeout))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      if self.relative is None:
        self.relative = experiments.msg.MoveRelative()
      if self.pattern is None:
        self.pattern = experiments.msg.MovePattern()
      end = 0
      start = end
      end += 1
      (self.enabled,) = _struct_B.unpack(str[start:end])
      self.enabled = bool(self.enabled)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.mode = str[start:end]
      start = end
      end += 1
      (self.relative.tracking,) = _struct_B.unpack(str[start:end])
      self.relative.tracking = bool(self.relative.tracking)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.relative.frameidOriginPosition = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.relative.frameidOriginAngle = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.relative.distance, _x.relative.angle,) = _struct_2d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.relative.angleType = str[start:end]
      start = end
      end += 8
      (self.relative.speed,) = _struct_d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.relative.speedType = str[start:end]
      start = end
      end += 8
      (self.relative.tolerance,) = _struct_d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.pattern.shape = str[start:end]
      _x = self
      start = end
      end += 28
      (_x.pattern.hz, _x.pattern.count, _x.pattern.radius, _x.timeout,) = _struct_di2d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      buff.write(_struct_B.pack(self.enabled))
      _x = self.mode
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.relative.tracking))
      _x = self.relative.frameidOriginPosition
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.relative.frameidOriginAngle
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2d.pack(_x.relative.distance, _x.relative.angle))
      _x = self.relative.angleType
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_d.pack(self.relative.speed))
      _x = self.relative.speedType
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_d.pack(self.relative.tolerance))
      _x = self.pattern.shape
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_di2d.pack(_x.pattern.hz, _x.pattern.count, _x.pattern.radius, _x.timeout))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      if self.relative is None:
        self.relative = experiments.msg.MoveRelative()
      if self.pattern is None:
        self.pattern = experiments.msg.MovePattern()
      end = 0
      start = end
      end += 1
      (self.enabled,) = _struct_B.unpack(str[start:end])
      self.enabled = bool(self.enabled)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.mode = str[start:end]
      start = end
      end += 1
      (self.relative.tracking,) = _struct_B.unpack(str[start:end])
      self.relative.tracking = bool(self.relative.tracking)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.relative.frameidOriginPosition = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.relative.frameidOriginAngle = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.relative.distance, _x.relative.angle,) = _struct_2d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.relative.angleType = str[start:end]
      start = end
      end += 8
      (self.relative.speed,) = _struct_d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.relative.speedType = str[start:end]
      start = end
      end += 8
      (self.relative.tolerance,) = _struct_d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.pattern.shape = str[start:end]
      _x = self
      start = end
      end += 28
      (_x.pattern.hz, _x.pattern.count, _x.pattern.radius, _x.timeout,) = _struct_di2d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_2d = struct.Struct("<2d")
_struct_B = struct.Struct("<B")
_struct_d = struct.Struct("<d")
_struct_di2d = struct.Struct("<di2d")

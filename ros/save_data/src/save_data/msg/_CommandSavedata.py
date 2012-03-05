"""autogenerated by genmsg_py from CommandSavedata.msg. Do not edit."""
import roslib.message
import struct


class CommandSavedata(roslib.message.Message):
  _md5sum = "cd82600eeba52d4a8018b7b5c960977a"
  _type = "save_data/CommandSavedata"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string filename
bool save_arenastate
bool save_video
bool save_bag

#string protocol
#int32 trial_number
#float64 angular_velocity_goal
#bool rm_file

"""
  __slots__ = ['filename','save_arenastate','save_video','save_bag']
  _slot_types = ['string','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       filename,save_arenastate,save_video,save_bag
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(CommandSavedata, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.filename is None:
        self.filename = ''
      if self.save_arenastate is None:
        self.save_arenastate = False
      if self.save_video is None:
        self.save_video = False
      if self.save_bag is None:
        self.save_bag = False
    else:
      self.filename = ''
      self.save_arenastate = False
      self.save_video = False
      self.save_bag = False

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
      _x = self.filename
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3B.pack(_x.save_arenastate, _x.save_video, _x.save_bag))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.filename = str[start:end]
      _x = self
      start = end
      end += 3
      (_x.save_arenastate, _x.save_video, _x.save_bag,) = _struct_3B.unpack(str[start:end])
      self.save_arenastate = bool(self.save_arenastate)
      self.save_video = bool(self.save_video)
      self.save_bag = bool(self.save_bag)
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
      _x = self.filename
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3B.pack(_x.save_arenastate, _x.save_video, _x.save_bag))
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
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.filename = str[start:end]
      _x = self
      start = end
      end += 3
      (_x.save_arenastate, _x.save_video, _x.save_bag,) = _struct_3B.unpack(str[start:end])
      self.save_arenastate = bool(self.save_arenastate)
      self.save_video = bool(self.save_video)
      self.save_bag = bool(self.save_bag)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_3B = struct.Struct("<3B")

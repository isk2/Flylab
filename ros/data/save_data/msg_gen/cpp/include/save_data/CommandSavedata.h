/* Auto-generated by genmsg_cpp for file /home/ssafarik/git/Flyatar2/ros/data/save_data/msg/CommandSavedata.msg */
#ifndef SAVE_DATA_MESSAGE_COMMANDSAVEDATA_H
#define SAVE_DATA_MESSAGE_COMMANDSAVEDATA_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"


namespace save_data
{
template <class ContainerAllocator>
struct CommandSavedata_ {
  typedef CommandSavedata_<ContainerAllocator> Type;

  CommandSavedata_()
  : filename()
  , save_arenastate(false)
  , save_video(false)
  , save_bag(false)
  {
  }

  CommandSavedata_(const ContainerAllocator& _alloc)
  : filename(_alloc)
  , save_arenastate(false)
  , save_video(false)
  , save_bag(false)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _filename_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  filename;

  typedef uint8_t _save_arenastate_type;
  uint8_t save_arenastate;

  typedef uint8_t _save_video_type;
  uint8_t save_video;

  typedef uint8_t _save_bag_type;
  uint8_t save_bag;


private:
  static const char* __s_getDataType_() { return "save_data/CommandSavedata"; }
public:
  ROS_DEPRECATED static const std::string __s_getDataType() { return __s_getDataType_(); }

  ROS_DEPRECATED const std::string __getDataType() const { return __s_getDataType_(); }

private:
  static const char* __s_getMD5Sum_() { return "cd82600eeba52d4a8018b7b5c960977a"; }
public:
  ROS_DEPRECATED static const std::string __s_getMD5Sum() { return __s_getMD5Sum_(); }

  ROS_DEPRECATED const std::string __getMD5Sum() const { return __s_getMD5Sum_(); }

private:
  static const char* __s_getMessageDefinition_() { return "string filename\n\
bool save_arenastate\n\
bool save_video\n\
bool save_bag\n\
\n\
#string protocol\n\
#int32 trial_number\n\
#float64 angular_velocity_goal\n\
#bool rm_file\n\
\n\
"; }
public:
  ROS_DEPRECATED static const std::string __s_getMessageDefinition() { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED const std::string __getMessageDefinition() const { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED virtual uint8_t *serialize(uint8_t *write_ptr, uint32_t seq) const
  {
    ros::serialization::OStream stream(write_ptr, 1000000000);
    ros::serialization::serialize(stream, filename);
    ros::serialization::serialize(stream, save_arenastate);
    ros::serialization::serialize(stream, save_video);
    ros::serialization::serialize(stream, save_bag);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    ros::serialization::IStream stream(read_ptr, 1000000000);
    ros::serialization::deserialize(stream, filename);
    ros::serialization::deserialize(stream, save_arenastate);
    ros::serialization::deserialize(stream, save_video);
    ros::serialization::deserialize(stream, save_bag);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint32_t serializationLength() const
  {
    uint32_t size = 0;
    size += ros::serialization::serializationLength(filename);
    size += ros::serialization::serializationLength(save_arenastate);
    size += ros::serialization::serializationLength(save_video);
    size += ros::serialization::serializationLength(save_bag);
    return size;
  }

  typedef boost::shared_ptr< ::save_data::CommandSavedata_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::save_data::CommandSavedata_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct CommandSavedata
typedef  ::save_data::CommandSavedata_<std::allocator<void> > CommandSavedata;

typedef boost::shared_ptr< ::save_data::CommandSavedata> CommandSavedataPtr;
typedef boost::shared_ptr< ::save_data::CommandSavedata const> CommandSavedataConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::save_data::CommandSavedata_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::save_data::CommandSavedata_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace save_data

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::save_data::CommandSavedata_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::save_data::CommandSavedata_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::save_data::CommandSavedata_<ContainerAllocator> > {
  static const char* value() 
  {
    return "cd82600eeba52d4a8018b7b5c960977a";
  }

  static const char* value(const  ::save_data::CommandSavedata_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xcd82600eeba52d4aULL;
  static const uint64_t static_value2 = 0x8018b7b5c960977aULL;
};

template<class ContainerAllocator>
struct DataType< ::save_data::CommandSavedata_<ContainerAllocator> > {
  static const char* value() 
  {
    return "save_data/CommandSavedata";
  }

  static const char* value(const  ::save_data::CommandSavedata_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::save_data::CommandSavedata_<ContainerAllocator> > {
  static const char* value() 
  {
    return "string filename\n\
bool save_arenastate\n\
bool save_video\n\
bool save_bag\n\
\n\
#string protocol\n\
#int32 trial_number\n\
#float64 angular_velocity_goal\n\
#bool rm_file\n\
\n\
";
  }

  static const char* value(const  ::save_data::CommandSavedata_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::save_data::CommandSavedata_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.filename);
    stream.next(m.save_arenastate);
    stream.next(m.save_video);
    stream.next(m.save_bag);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct CommandSavedata_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::save_data::CommandSavedata_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::save_data::CommandSavedata_<ContainerAllocator> & v) 
  {
    s << indent << "filename: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.filename);
    s << indent << "save_arenastate: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.save_arenastate);
    s << indent << "save_video: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.save_video);
    s << indent << "save_bag: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.save_bag);
  }
};


} // namespace message_operations
} // namespace ros

#endif // SAVE_DATA_MESSAGE_COMMANDSAVEDATA_H


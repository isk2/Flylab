/* Auto-generated by genmsg_cpp for file /home/ssafarik/git/Flyatar2/ros/experiments/msg/TriggerSettings.msg */
#ifndef EXPERIMENTS_MESSAGE_TRIGGERSETTINGS_H
#define EXPERIMENTS_MESSAGE_TRIGGERSETTINGS_H
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


namespace experiments
{
template <class ContainerAllocator>
struct TriggerSettings_ {
  typedef TriggerSettings_<ContainerAllocator> Type;

  TriggerSettings_()
  : enabled(false)
  , distanceMin(0.0)
  , distanceMax(0.0)
  , speedMin(0.0)
  , speedMax(0.0)
  , angleMin(0.0)
  , angleMax(0.0)
  , angleTest()
  , angleTestBilateral(false)
  , timeHold(0.0)
  , timeout(0.0)
  {
  }

  TriggerSettings_(const ContainerAllocator& _alloc)
  : enabled(false)
  , distanceMin(0.0)
  , distanceMax(0.0)
  , speedMin(0.0)
  , speedMax(0.0)
  , angleMin(0.0)
  , angleMax(0.0)
  , angleTest(_alloc)
  , angleTestBilateral(false)
  , timeHold(0.0)
  , timeout(0.0)
  {
  }

  typedef uint8_t _enabled_type;
  uint8_t enabled;

  typedef double _distanceMin_type;
  double distanceMin;

  typedef double _distanceMax_type;
  double distanceMax;

  typedef double _speedMin_type;
  double speedMin;

  typedef double _speedMax_type;
  double speedMax;

  typedef double _angleMin_type;
  double angleMin;

  typedef double _angleMax_type;
  double angleMax;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _angleTest_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  angleTest;

  typedef uint8_t _angleTestBilateral_type;
  uint8_t angleTestBilateral;

  typedef double _timeHold_type;
  double timeHold;

  typedef double _timeout_type;
  double timeout;


private:
  static const char* __s_getDataType_() { return "experiments/TriggerSettings"; }
public:
  ROS_DEPRECATED static const std::string __s_getDataType() { return __s_getDataType_(); }

  ROS_DEPRECATED const std::string __getDataType() const { return __s_getDataType_(); }

private:
  static const char* __s_getMD5Sum_() { return "009cb593fc0cecc966de010b763b71c1"; }
public:
  ROS_DEPRECATED static const std::string __s_getMD5Sum() { return __s_getMD5Sum_(); }

  ROS_DEPRECATED const std::string __getMD5Sum() const { return __s_getMD5Sum_(); }

private:
  static const char* __s_getMessageDefinition_() { return "bool enabled\n\
float64 distanceMin\n\
float64 distanceMax\n\
float64 speedMin\n\
float64 speedMax\n\
float64 angleMin\n\
float64 angleMax\n\
string  angleTest\n\
bool    angleTestBilateral\n\
float64 timeHold\n\
float64 timeout\n\
\n\
\n\
\n\
"; }
public:
  ROS_DEPRECATED static const std::string __s_getMessageDefinition() { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED const std::string __getMessageDefinition() const { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED virtual uint8_t *serialize(uint8_t *write_ptr, uint32_t seq) const
  {
    ros::serialization::OStream stream(write_ptr, 1000000000);
    ros::serialization::serialize(stream, enabled);
    ros::serialization::serialize(stream, distanceMin);
    ros::serialization::serialize(stream, distanceMax);
    ros::serialization::serialize(stream, speedMin);
    ros::serialization::serialize(stream, speedMax);
    ros::serialization::serialize(stream, angleMin);
    ros::serialization::serialize(stream, angleMax);
    ros::serialization::serialize(stream, angleTest);
    ros::serialization::serialize(stream, angleTestBilateral);
    ros::serialization::serialize(stream, timeHold);
    ros::serialization::serialize(stream, timeout);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    ros::serialization::IStream stream(read_ptr, 1000000000);
    ros::serialization::deserialize(stream, enabled);
    ros::serialization::deserialize(stream, distanceMin);
    ros::serialization::deserialize(stream, distanceMax);
    ros::serialization::deserialize(stream, speedMin);
    ros::serialization::deserialize(stream, speedMax);
    ros::serialization::deserialize(stream, angleMin);
    ros::serialization::deserialize(stream, angleMax);
    ros::serialization::deserialize(stream, angleTest);
    ros::serialization::deserialize(stream, angleTestBilateral);
    ros::serialization::deserialize(stream, timeHold);
    ros::serialization::deserialize(stream, timeout);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint32_t serializationLength() const
  {
    uint32_t size = 0;
    size += ros::serialization::serializationLength(enabled);
    size += ros::serialization::serializationLength(distanceMin);
    size += ros::serialization::serializationLength(distanceMax);
    size += ros::serialization::serializationLength(speedMin);
    size += ros::serialization::serializationLength(speedMax);
    size += ros::serialization::serializationLength(angleMin);
    size += ros::serialization::serializationLength(angleMax);
    size += ros::serialization::serializationLength(angleTest);
    size += ros::serialization::serializationLength(angleTestBilateral);
    size += ros::serialization::serializationLength(timeHold);
    size += ros::serialization::serializationLength(timeout);
    return size;
  }

  typedef boost::shared_ptr< ::experiments::TriggerSettings_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::experiments::TriggerSettings_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct TriggerSettings
typedef  ::experiments::TriggerSettings_<std::allocator<void> > TriggerSettings;

typedef boost::shared_ptr< ::experiments::TriggerSettings> TriggerSettingsPtr;
typedef boost::shared_ptr< ::experiments::TriggerSettings const> TriggerSettingsConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::experiments::TriggerSettings_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::experiments::TriggerSettings_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace experiments

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::experiments::TriggerSettings_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::experiments::TriggerSettings_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::experiments::TriggerSettings_<ContainerAllocator> > {
  static const char* value() 
  {
    return "009cb593fc0cecc966de010b763b71c1";
  }

  static const char* value(const  ::experiments::TriggerSettings_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x009cb593fc0cecc9ULL;
  static const uint64_t static_value2 = 0x66de010b763b71c1ULL;
};

template<class ContainerAllocator>
struct DataType< ::experiments::TriggerSettings_<ContainerAllocator> > {
  static const char* value() 
  {
    return "experiments/TriggerSettings";
  }

  static const char* value(const  ::experiments::TriggerSettings_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::experiments::TriggerSettings_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool enabled\n\
float64 distanceMin\n\
float64 distanceMax\n\
float64 speedMin\n\
float64 speedMax\n\
float64 angleMin\n\
float64 angleMax\n\
string  angleTest\n\
bool    angleTestBilateral\n\
float64 timeHold\n\
float64 timeout\n\
\n\
\n\
\n\
";
  }

  static const char* value(const  ::experiments::TriggerSettings_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::experiments::TriggerSettings_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.enabled);
    stream.next(m.distanceMin);
    stream.next(m.distanceMax);
    stream.next(m.speedMin);
    stream.next(m.speedMax);
    stream.next(m.angleMin);
    stream.next(m.angleMax);
    stream.next(m.angleTest);
    stream.next(m.angleTestBilateral);
    stream.next(m.timeHold);
    stream.next(m.timeout);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct TriggerSettings_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::experiments::TriggerSettings_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::experiments::TriggerSettings_<ContainerAllocator> & v) 
  {
    s << indent << "enabled: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.enabled);
    s << indent << "distanceMin: ";
    Printer<double>::stream(s, indent + "  ", v.distanceMin);
    s << indent << "distanceMax: ";
    Printer<double>::stream(s, indent + "  ", v.distanceMax);
    s << indent << "speedMin: ";
    Printer<double>::stream(s, indent + "  ", v.speedMin);
    s << indent << "speedMax: ";
    Printer<double>::stream(s, indent + "  ", v.speedMax);
    s << indent << "angleMin: ";
    Printer<double>::stream(s, indent + "  ", v.angleMin);
    s << indent << "angleMax: ";
    Printer<double>::stream(s, indent + "  ", v.angleMax);
    s << indent << "angleTest: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.angleTest);
    s << indent << "angleTestBilateral: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.angleTestBilateral);
    s << indent << "timeHold: ";
    Printer<double>::stream(s, indent + "  ", v.timeHold);
    s << indent << "timeout: ";
    Printer<double>::stream(s, indent + "  ", v.timeout);
  }
};


} // namespace message_operations
} // namespace ros

#endif // EXPERIMENTS_MESSAGE_TRIGGERSETTINGS_H


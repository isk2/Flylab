/* Auto-generated by genmsg_cpp for file /home/ssafarik/git/Flyatar2/ros/experiments/srv/ExperimentParams.srv */
#ifndef EXPERIMENTS_SERVICE_EXPERIMENTPARAMS_H
#define EXPERIMENTS_SERVICE_EXPERIMENTPARAMS_H
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

#include "ros/service_traits.h"

#include "experiments/ExperimentSettings.h"
#include "experiments/HomeSettings.h"
#include "experiments/TriggerSettings.h"
#include "experiments/MoveSettings.h"
#include "experiments/TriggerSettings.h"
#include "experiments/SaveSettings.h"



namespace experiments
{
template <class ContainerAllocator>
struct ExperimentParamsRequest_ {
  typedef ExperimentParamsRequest_<ContainerAllocator> Type;

  ExperimentParamsRequest_()
  : experiment()
  , home()
  , waitEntry(0.0)
  , triggerEntry()
  , move()
  , triggerExit()
  , save()
  {
  }

  ExperimentParamsRequest_(const ContainerAllocator& _alloc)
  : experiment(_alloc)
  , home(_alloc)
  , waitEntry(0.0)
  , triggerEntry(_alloc)
  , move(_alloc)
  , triggerExit(_alloc)
  , save(_alloc)
  {
  }

  typedef  ::experiments::ExperimentSettings_<ContainerAllocator>  _experiment_type;
   ::experiments::ExperimentSettings_<ContainerAllocator>  experiment;

  typedef  ::experiments::HomeSettings_<ContainerAllocator>  _home_type;
   ::experiments::HomeSettings_<ContainerAllocator>  home;

  typedef double _waitEntry_type;
  double waitEntry;

  typedef  ::experiments::TriggerSettings_<ContainerAllocator>  _triggerEntry_type;
   ::experiments::TriggerSettings_<ContainerAllocator>  triggerEntry;

  typedef  ::experiments::MoveSettings_<ContainerAllocator>  _move_type;
   ::experiments::MoveSettings_<ContainerAllocator>  move;

  typedef  ::experiments::TriggerSettings_<ContainerAllocator>  _triggerExit_type;
   ::experiments::TriggerSettings_<ContainerAllocator>  triggerExit;

  typedef  ::experiments::SaveSettings_<ContainerAllocator>  _save_type;
   ::experiments::SaveSettings_<ContainerAllocator>  save;


private:
  static const char* __s_getDataType_() { return "experiments/ExperimentParamsRequest"; }
public:
  ROS_DEPRECATED static const std::string __s_getDataType() { return __s_getDataType_(); }

  ROS_DEPRECATED const std::string __getDataType() const { return __s_getDataType_(); }

private:
  static const char* __s_getMD5Sum_() { return "df5f51a0f1107bf71a39897277548aa5"; }
public:
  ROS_DEPRECATED static const std::string __s_getMD5Sum() { return __s_getMD5Sum_(); }

  ROS_DEPRECATED const std::string __getMD5Sum() const { return __s_getMD5Sum_(); }

private:
  static const char* __s_getServerMD5Sum_() { return "5808c8ba5652d03d7168883a279eaa4a"; }
public:
  ROS_DEPRECATED static const std::string __s_getServerMD5Sum() { return __s_getServerMD5Sum_(); }

  ROS_DEPRECATED const std::string __getServerMD5Sum() const { return __s_getServerMD5Sum_(); }

private:
  static const char* __s_getMessageDefinition_() { return "ExperimentSettings experiment\n\
HomeSettings home\n\
float64 waitEntry\n\
TriggerSettings triggerEntry\n\
MoveSettings move\n\
TriggerSettings triggerExit\n\
SaveSettings save\n\
\n\
================================================================================\n\
MSG: experiments/ExperimentSettings\n\
string description\n\
int32 maxTrials\n\
int32 trial \n\
\n\
\n\
================================================================================\n\
MSG: experiments/HomeSettings\n\
bool enabled\n\
float64 x\n\
float64 y\n\
float64 tolerance\n\
float64 timeout\n\
\n\
\n\
\n\
================================================================================\n\
MSG: experiments/TriggerSettings\n\
bool enabled\n\
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
================================================================================\n\
MSG: experiments/MoveSettings\n\
bool enabled\n\
string mode  # 'pattern' or 'relative'\n\
MoveRelative relative\n\
MovePattern pattern\n\
float64 timeout\n\
\n\
\n\
================================================================================\n\
MSG: experiments/MoveRelative\n\
bool tracking\n\
string frameidOriginPosition # 'Plate' or 'Robot' or 'Fly'\n\
string frameidOriginAngle # 'Plate' or 'Robot' or 'Fly'\n\
float64 distance\n\
float64 angle\n\
string angleType # 'random' or 'constant'\n\
float64 speed\n\
string speedType # 'random' or 'constant'\n\
float64 tolerance\n\
\n\
\n\
================================================================================\n\
MSG: experiments/MovePattern\n\
string shape  # 'constant' or 'circle' or 'square' or 'flylogo' or 'spiral'\n\
float64 hz\n\
int32 count  # -1 means forever\n\
float64 radius\n\
\n\
\n\
================================================================================\n\
MSG: experiments/SaveSettings\n\
string filenamebase\n\
bool arenastate\n\
bool video\n\
bool bag\n\
bool onlyWhileTriggered\n\
\n\
\n\
"; }
public:
  ROS_DEPRECATED static const std::string __s_getMessageDefinition() { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED const std::string __getMessageDefinition() const { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED virtual uint8_t *serialize(uint8_t *write_ptr, uint32_t seq) const
  {
    ros::serialization::OStream stream(write_ptr, 1000000000);
    ros::serialization::serialize(stream, experiment);
    ros::serialization::serialize(stream, home);
    ros::serialization::serialize(stream, waitEntry);
    ros::serialization::serialize(stream, triggerEntry);
    ros::serialization::serialize(stream, move);
    ros::serialization::serialize(stream, triggerExit);
    ros::serialization::serialize(stream, save);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    ros::serialization::IStream stream(read_ptr, 1000000000);
    ros::serialization::deserialize(stream, experiment);
    ros::serialization::deserialize(stream, home);
    ros::serialization::deserialize(stream, waitEntry);
    ros::serialization::deserialize(stream, triggerEntry);
    ros::serialization::deserialize(stream, move);
    ros::serialization::deserialize(stream, triggerExit);
    ros::serialization::deserialize(stream, save);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint32_t serializationLength() const
  {
    uint32_t size = 0;
    size += ros::serialization::serializationLength(experiment);
    size += ros::serialization::serializationLength(home);
    size += ros::serialization::serializationLength(waitEntry);
    size += ros::serialization::serializationLength(triggerEntry);
    size += ros::serialization::serializationLength(move);
    size += ros::serialization::serializationLength(triggerExit);
    size += ros::serialization::serializationLength(save);
    return size;
  }

  typedef boost::shared_ptr< ::experiments::ExperimentParamsRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::experiments::ExperimentParamsRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ExperimentParamsRequest
typedef  ::experiments::ExperimentParamsRequest_<std::allocator<void> > ExperimentParamsRequest;

typedef boost::shared_ptr< ::experiments::ExperimentParamsRequest> ExperimentParamsRequestPtr;
typedef boost::shared_ptr< ::experiments::ExperimentParamsRequest const> ExperimentParamsRequestConstPtr;


template <class ContainerAllocator>
struct ExperimentParamsResponse_ {
  typedef ExperimentParamsResponse_<ContainerAllocator> Type;

  ExperimentParamsResponse_()
  : succeeded(false)
  {
  }

  ExperimentParamsResponse_(const ContainerAllocator& _alloc)
  : succeeded(false)
  {
  }

  typedef uint8_t _succeeded_type;
  uint8_t succeeded;


private:
  static const char* __s_getDataType_() { return "experiments/ExperimentParamsResponse"; }
public:
  ROS_DEPRECATED static const std::string __s_getDataType() { return __s_getDataType_(); }

  ROS_DEPRECATED const std::string __getDataType() const { return __s_getDataType_(); }

private:
  static const char* __s_getMD5Sum_() { return "95e696a0d10686913abb262e0b4cbbcf"; }
public:
  ROS_DEPRECATED static const std::string __s_getMD5Sum() { return __s_getMD5Sum_(); }

  ROS_DEPRECATED const std::string __getMD5Sum() const { return __s_getMD5Sum_(); }

private:
  static const char* __s_getServerMD5Sum_() { return "5808c8ba5652d03d7168883a279eaa4a"; }
public:
  ROS_DEPRECATED static const std::string __s_getServerMD5Sum() { return __s_getServerMD5Sum_(); }

  ROS_DEPRECATED const std::string __getServerMD5Sum() const { return __s_getServerMD5Sum_(); }

private:
  static const char* __s_getMessageDefinition_() { return "bool succeeded\n\
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
    ros::serialization::serialize(stream, succeeded);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    ros::serialization::IStream stream(read_ptr, 1000000000);
    ros::serialization::deserialize(stream, succeeded);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint32_t serializationLength() const
  {
    uint32_t size = 0;
    size += ros::serialization::serializationLength(succeeded);
    return size;
  }

  typedef boost::shared_ptr< ::experiments::ExperimentParamsResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::experiments::ExperimentParamsResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ExperimentParamsResponse
typedef  ::experiments::ExperimentParamsResponse_<std::allocator<void> > ExperimentParamsResponse;

typedef boost::shared_ptr< ::experiments::ExperimentParamsResponse> ExperimentParamsResponsePtr;
typedef boost::shared_ptr< ::experiments::ExperimentParamsResponse const> ExperimentParamsResponseConstPtr;

struct ExperimentParams
{

typedef ExperimentParamsRequest Request;
typedef ExperimentParamsResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct ExperimentParams
} // namespace experiments

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::experiments::ExperimentParamsRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::experiments::ExperimentParamsRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::experiments::ExperimentParamsRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "df5f51a0f1107bf71a39897277548aa5";
  }

  static const char* value(const  ::experiments::ExperimentParamsRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xdf5f51a0f1107bf7ULL;
  static const uint64_t static_value2 = 0x1a39897277548aa5ULL;
};

template<class ContainerAllocator>
struct DataType< ::experiments::ExperimentParamsRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "experiments/ExperimentParamsRequest";
  }

  static const char* value(const  ::experiments::ExperimentParamsRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::experiments::ExperimentParamsRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "ExperimentSettings experiment\n\
HomeSettings home\n\
float64 waitEntry\n\
TriggerSettings triggerEntry\n\
MoveSettings move\n\
TriggerSettings triggerExit\n\
SaveSettings save\n\
\n\
================================================================================\n\
MSG: experiments/ExperimentSettings\n\
string description\n\
int32 maxTrials\n\
int32 trial \n\
\n\
\n\
================================================================================\n\
MSG: experiments/HomeSettings\n\
bool enabled\n\
float64 x\n\
float64 y\n\
float64 tolerance\n\
float64 timeout\n\
\n\
\n\
\n\
================================================================================\n\
MSG: experiments/TriggerSettings\n\
bool enabled\n\
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
================================================================================\n\
MSG: experiments/MoveSettings\n\
bool enabled\n\
string mode  # 'pattern' or 'relative'\n\
MoveRelative relative\n\
MovePattern pattern\n\
float64 timeout\n\
\n\
\n\
================================================================================\n\
MSG: experiments/MoveRelative\n\
bool tracking\n\
string frameidOriginPosition # 'Plate' or 'Robot' or 'Fly'\n\
string frameidOriginAngle # 'Plate' or 'Robot' or 'Fly'\n\
float64 distance\n\
float64 angle\n\
string angleType # 'random' or 'constant'\n\
float64 speed\n\
string speedType # 'random' or 'constant'\n\
float64 tolerance\n\
\n\
\n\
================================================================================\n\
MSG: experiments/MovePattern\n\
string shape  # 'constant' or 'circle' or 'square' or 'flylogo' or 'spiral'\n\
float64 hz\n\
int32 count  # -1 means forever\n\
float64 radius\n\
\n\
\n\
================================================================================\n\
MSG: experiments/SaveSettings\n\
string filenamebase\n\
bool arenastate\n\
bool video\n\
bool bag\n\
bool onlyWhileTriggered\n\
\n\
\n\
";
  }

  static const char* value(const  ::experiments::ExperimentParamsRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::experiments::ExperimentParamsResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::experiments::ExperimentParamsResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::experiments::ExperimentParamsResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "95e696a0d10686913abb262e0b4cbbcf";
  }

  static const char* value(const  ::experiments::ExperimentParamsResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x95e696a0d1068691ULL;
  static const uint64_t static_value2 = 0x3abb262e0b4cbbcfULL;
};

template<class ContainerAllocator>
struct DataType< ::experiments::ExperimentParamsResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "experiments/ExperimentParamsResponse";
  }

  static const char* value(const  ::experiments::ExperimentParamsResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::experiments::ExperimentParamsResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool succeeded\n\
\n\
\n\
\n\
";
  }

  static const char* value(const  ::experiments::ExperimentParamsResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::experiments::ExperimentParamsResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::experiments::ExperimentParamsRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.experiment);
    stream.next(m.home);
    stream.next(m.waitEntry);
    stream.next(m.triggerEntry);
    stream.next(m.move);
    stream.next(m.triggerExit);
    stream.next(m.save);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ExperimentParamsRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::experiments::ExperimentParamsResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.succeeded);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ExperimentParamsResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<experiments::ExperimentParams> {
  static const char* value() 
  {
    return "5808c8ba5652d03d7168883a279eaa4a";
  }

  static const char* value(const experiments::ExperimentParams&) { return value(); } 
};

template<>
struct DataType<experiments::ExperimentParams> {
  static const char* value() 
  {
    return "experiments/ExperimentParams";
  }

  static const char* value(const experiments::ExperimentParams&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<experiments::ExperimentParamsRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "5808c8ba5652d03d7168883a279eaa4a";
  }

  static const char* value(const experiments::ExperimentParamsRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<experiments::ExperimentParamsRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "experiments/ExperimentParams";
  }

  static const char* value(const experiments::ExperimentParamsRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<experiments::ExperimentParamsResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "5808c8ba5652d03d7168883a279eaa4a";
  }

  static const char* value(const experiments::ExperimentParamsResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<experiments::ExperimentParamsResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "experiments/ExperimentParams";
  }

  static const char* value(const experiments::ExperimentParamsResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // EXPERIMENTS_SERVICE_EXPERIMENTPARAMS_H


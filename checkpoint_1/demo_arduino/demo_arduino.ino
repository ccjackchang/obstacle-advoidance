#include <ros.h>
#include <std_msgs/Int32.h>

ros::NodeHandle nh;

std_msgs::Int32 msg_pub;
ros::Publisher pub("/arduino_numbers", &msg_pub);

int count = 0;

void rpi_cb(const std_msgs::Int32& output_msg)
{
  msg_pub.data = output_msg.data * 2;
  count += 1;
}

ros::Subscriber<std_msgs::Int32> msg_sub("/rpi_numbers", rpi_cb);

void setup()
{
  Serial.begin(57600);

  nh.initNode();
  nh.subscribe(msg_sub);
  nh.advertise(pub);
}

void loop()
{
  if(count >= 20) pub.publish(&msg_pub);
  nh.spinOnce();
  delay(100);
}

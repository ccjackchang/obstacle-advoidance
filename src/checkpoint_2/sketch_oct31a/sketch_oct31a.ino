
#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle nh;

// 設定 PWM 輸出值
int8_t speed1 = 0;
int8_t speed2 = 0;
const byte EA = 9; // 馬達 A 的致能接腳
const byte IA1 = 4; // 馬達 A 的正轉接腳
const byte IA2 = 5; // 馬達 A 的反轉接腳
const byte EB = 10; // 馬達 B 的接腳
const byte IB1 = 6; // 馬達 B 的正轉接腳
const byte IB2 = 7; // 馬達 B 的反轉接腳
#define PIN_LIGHT A3
unsigned long t_stamp;
const int INTERVEL_LIGHT_MS = 500;

std_msgs::Int16 light_msg;
ros::Publisher pub_light_val("light_value", &light_msg);

void messageCb1( const std_msgs::Int16& arg1){
  speed1 = arg1.data;
}

ros::Subscriber<std_msgs::Int16> sub1("pwm1", &messageCb1 );

void messageCb2( const std_msgs::Int16& arg2){
  speed2 = arg2.data;
}

ros::Subscriber<std_msgs::Int16> sub2("pwm2", &messageCb2 );


void go() { // 馬達轉向
if (speed1 >= 0) {
    digitalWrite(IA1, LOW);
    digitalWrite(IA2, HIGH);
}
else{
    digitalWrite(IA1, HIGH);
    digitalWrite(IA2, LOW);
}
if (speed2 >= 0){
    digitalWrite(IB1, HIGH);
    digitalWrite(IB2, LOW);
}
else{
    digitalWrite(IB1, LOW);
    digitalWrite(IB2, HIGH);
}
    analogWrite(EA, abs(speed1)); // 馬達 A 的 PWM 輸出
    analogWrite(EB, abs(speed2)); // 馬達 B 的 PWM 輸出

if((millis() -t_stamp) > INTERVEL_LIGHT_MS){
    light_msg.data = analogRead(PIN_LIGHT);
    pub_light_val.publish(&light_msg);
    t_stamp = millis();
  }


}



void setup() {
Serial.begin(115200); // 啟動軟體序列埠
pinMode(EA, OUTPUT);
pinMode(EB, OUTPUT);
pinMode(IA1, OUTPUT); 
pinMode(IA2, OUTPUT);
pinMode(IB1, OUTPUT); 
pinMode(IB2, OUTPUT);
nh.initNode();
nh.subscribe(sub1);
nh.subscribe(sub2);
nh.advertise(pub_light_val);
t_stamp = millis();
}

void loop() {
go();
nh.spinOnce();
}

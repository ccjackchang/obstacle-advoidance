#!/usr/bin/env python
import rospy

from std_msgs.msg import Int16
import sys, select, termios, tty

def go():
	pub1 = rospy.Publisher('/pwm1', Int16, queue_size=5)
	pub2 = rospy.Publisher('/pwm2', Int16, queue_size=5)
	rospy.init_node('motor_control')
	rate = rospy.Rate(10)


	while not rospy.is_shutdown():
		pwm1 = input("Please input left wheel PWM :")
		pwm2 = input("Please input right wheel PWM :")
		pub1.publish(pwm1)
		pub2.publish(pwm2)
		rate.sleep()

	pwm1 = 0
	pwm2 = 0
	print "pwm1 =",pwm1
	print "pwm2 =",pwm2
	pub1.publish(pwm1)
	pub2.publish(pwm2)

if __name__=='__main__':
	try:
		go()
	except rospy.ROSInterruptException:
		pass


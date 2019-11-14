#!/usr/bin/env python
import rospy

from std_msgs.msg import UInt8
import sys, select, termios, tty

def data():
	pub = rospy.Publisher('/command', UInt8, queue_size=5)
	pub1 = rospy.Publisher('/pwm1', UInt8, queue_size=5)
	pub2 = rospy.Publisher('/pwm2', UInt8, queue_size=5)
	rospy.init_node('turtlebot_teleop')
	rate = rospy.Rate(10)
	pwm1 = input("Please input left wheel PWM :")
	pwm2 = input("Please input right wheel PWM :")
	key_tmp = 0
	key = 0
	while not rospy.is_shutdown():
		tty.setraw(sys.stdin.fileno())
		key = sys.stdin.read(1)
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

		if key =='i':
			if (pwm1 <= 205 and pwm2 <= 205):
				pwm1 = pwm1 + 20
				pwm2 = pwm2 + 20
			else:
				pwm1 = pwm1
				pwm2 = pwm2
			print ("pwm1 =",pwm1)
			print ("pwm2 =",pwm2)
			pub1.publish(pwm1)
			pub2.publish(pwm2)
		if key =='o':
			if (pwm1 <= 205 and pwm2 <= 205):
				pwm1 = pwm1 + 10
				pwm2 = pwm2 + 20
			else:
				pwm1 = pwm1
				pwm2 = pwm2
			print ("pwm1 =",pwm1)
			print ("pwm2 =",pwm2)
			pub1.publish(pwm1)
			pub2.publish(pwm2)
		if key =='k':
			if (pwm1 >=20 and pwm2 >= 20):
				pwm1 = pwm1 - 20
				pwm2 = pwm2 - 20
			else:
				pwm1 = pwm1
				pwm2 = pwm2
			print ("pwm1 =",pwm1)
			print ("pwm2 =",pwm2)
			pub1.publish(pwm1)
			pub2.publish(pwm2)

		if key =='l':
			if (pwm1 >=20 and pwm2 >= 20):
				pwm1 = pwm1 - 10
				pwm2 = pwm2 - 20
			else:
				pwm1 = pwm1
				pwm2 = pwm2
			print ("pwm1 =",pwm1)
			print ("pwm2 =",pwm2)
			pub1.publish(pwm1)
			pub2.publish(pwm2)

		if key =='w':
		#	if (pwm1<pwm2):
		#		pwm2 = pwm1
		#		pub1.publish(pwm1)
		#		pub2.publish(pwm2)
		#	else:
		#		pwm1 = pwm2
			pub1.publish(pwm1)
			pub2.publish(pwm2)
			#print key
			pub.publish(1)
			rate.sleep()

		if key == 's':
			#print key
			pub.publish(5)
			pwm1 = input("Please input left wheel PWM :")
			pwm2 = input("Please input right wheel PWM :")
			rate.sleep()
		if key == 'a':
			#print key
			if (pwm1<pwm2):
				pwm2 = pwm1
				pub1.publish(pwm1)
				pub2.publish(pwm2)
			else:
				pwm1 = pwm2
				pub1.publish(pwm1)
				pub2.publish(pwm2)
			pub.publish(3)
			rate.sleep()
		if key == 'd':
			#print key
			if (pwm1<pwm2):
				pwm2 = pwm1
				pub1.publish(pwm1)
				pub2.publish(pwm2)
			else:
				pwm1 = pwm2
				pub1.publish(pwm1)
				pub2.publish(pwm2)
			pub.publish(4)
			rate.sleep()
		if key == 'x':
			#print key
			#if (pwm1<pwm2):
			#	pwm2 = pwm1
			#	pub1.publish(pwm1)
			#	pub2.publish(pwm2)
			#else:
			#	pwm1 = pwm2
			pub1.publish(pwm1)
			pub2.publish(pwm2)
			pub.publish(2)
			rate.sleep()

		if key == 'q':
			#print key
			if (pwm1<pwm2):
				pub1.publish(pwm1)
				pub2.publish(pwm2)
			elif(pwm1==pwm2):
				pub1.publish(pwm1)
				pub2.publish(pwm2+10)
			else:
				pwm1, pwm2 = pwm2, pwm1
				pub1.publish(pwm1)
				pub2.publish(pwm2)
			pub.publish(1)
			rate.sleep()

		if key == 'e':
			#print key
			if (pwm1>pwm2):
				pub1.publish(pwm1)
				pub2.publish(pwm2)
			elif(pwm1==pwm2):
				pub1.publish(pwm1+10)
				pub2.publish(pwm2)
			else:
				pwm1, pwm2 = pwm2, pwm1
				pub1.publish(pwm1)
				pub2.publish(pwm2)
			pub.publish(1)
			rate.sleep()

		if key == 'z':
			#print key
			if (pwm1<pwm2):
				pub1.publish(pwm1)
				pub2.publish(pwm2)
			elif(pwm1==pwm2):
				pub1.publish(pwm1)
				pub2.publish(pwm2+10)
			else:
				pwm1, pwm2 = pwm2, pwm1
				pub1.publish(pwm1)
				pub2.publish(pwm2)
			pub.publish(2)
			rate.sleep()

		if key == 'c':
			#print key
			if (pwm1>pwm2):
				pub1.publish(pwm1)
				pub2.publish(pwm2)
			elif(pwm1==pwm2):
				pub1.publish(pwm1+10)
				pub2.publish(pwm2)
			else:
				pwm1, pwm2 = pwm2, pwm1
				pub1.publish(pwm1)
				pub2.publish(pwm2)
			pub.publish(1)
			rate.sleep()
		if key == '':
			pub.publish(5)
			rate.sleep()
			pass

		if key == 'r':
			pub.publish(5)
			rate.sleep()
			break


if __name__=='__main__':
	try:
		settings = termios.tcgetattr(sys.stdin)
		data()
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	except rospy.ROSInterruptException:
		pass


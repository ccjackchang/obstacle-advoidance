#!/usr/bin/env python
import rospy
import wiringpi
import time
import math
from std_msgs.msg import Int16
import sys, select, termios, tty

class Main(): 
	def callback(self,data):
		self.i = data.data

	def lightcallback(self):
		rospy.Subscriber("/light_value", Int16, self.callback)
	
	def turn(self):
		pub1 = rospy.Publisher('/pwm1', Int16, queue_size=5)
		pub2 = rospy.Publisher('/pwm2', Int16, queue_size=5)
		rate = rospy.Rate(10)
		rospy.init_node('motor_control')
		a = datetime.datetime.now()
		b = float(a.second)+(float(a.microsecond)/1000000)
		c = a.second+1
		while (1):
			self.lightcallback()
			d = datetime.datetime.now()
			e = float(d.second)+(float(d.microsecond)/1000000)
			if(e<b):
				e = e + 60
			print "time=",(float(e-b))
			if float((e-b)<=(5) or (self.i <= 500): 
				pwm1 = 100
				pwm2 = -100
				pub1.publish(pwm1)
				pub2.publish(pwm2)
			else:
				break
		print "stop mode"
		pwm1 = 0
		pwm2 = 0
		pub1.publish(pwm1)
		pub2.publish(pwm2)
		time.sleep(1) 
		rate.sleep()

	def straight(self):
		pub1 = rospy.Publisher('/pwm1', Int16, queue_size=5)
		pub2 = rospy.Publisher('/pwm2', Int16, queue_size=5)
		rate = rospy.Rate(10)
		rospy.init_node('motor_control')
		a = datetime.datetime.now()
		b = float(a.second)+(float(a.microsecond)/1000000)
		c = a.second+1
		while (1):
			self.lightcallback()
			d = datetime.datetime.now()
			e = float(d.second)+(float(d.microsecond)/1000000)
			if(e<b):
				e = e + 60
			print "time=",(float(e-b))
			if float((e-b)<=(5) or (self.i <= 200): 
				pwm1 = 100
				pwm2 = 100
				pub1.publish(pwm1)
				pub2.publish(pwm2)
			else:
				break
		print "stop mode"
		pwm1 = 0
		pwm2 = 0
		pub1.publish(pwm1)
		pub2.publish(pwm2)
		time.sleep(1) 
		rate.sleep()

	def back(self):
		pub1 = rospy.Publisher('/pwm1', Int16, queue_size=5)
		pub2 = rospy.Publisher('/pwm2', Int16, queue_size=5)
		rate = rospy.Rate(10)
		rospy.init_node('motor_control')
		a = datetime.datetime.now()
		b = float(a.second)+(float(a.microsecond)/1000000)
		c = a.second+1
		while (1):
			self.lightcallback()
			d = datetime.datetime.now()
			e = float(d.second)+(float(d.microsecond)/1000000)
			if(e<b):
				e = e + 60
			print "time=",(float(e-b))
			if float((e-b)<=2: 
				pwm1 = -100
				pwm2 = -100
				pub1.publish(pwm1)
				pub2.publish(pwm2)
			else:
				break
		print "stop mode"
		pwm1 = 0
		pwm2 = 0
		pub1.publish(pwm1)
		pub2.publish(pwm2)
		time.sleep(1) 
		rate.sleep()

	def catch(self):
		wiringPiSetupGpio()
		wiringpi.pinMode(11,0)
		wiringpi.pinMode(13,0)
		wiringpi.pinMode(15,0)
		pub1 = rospy.Publisher('/pwm1', Int16, queue_size=5)
		pub2 = rospy.Publisher('/pwm2', Int16, queue_size=5)
		rospy.init_node('motor_control')
		rate = rospy.Rate(10)
		self.straight()
		while(1):
			ball = self.wiringpi.digitalRead(11)
			l = self.wiringpi.digitalRead(13)
			r = self.wiringpi.digitalRead(15)
			if (l = 1):
				self.back()
				self.turn()
				self.straight()
			if (r = 1):
				self.back()
				self.turn()
				self.straight()
			if (ball = 1):
				break
		time.sleep(1) 
		r.sleep()
 

if __name__=='__main__':
	main = Main()
	try:
		main.catch()
	except rospy.ROSInterruptException:
		pass


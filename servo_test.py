#!/usr/bin/env python

import easygopigo3 as easy
import time

gpg = easy.EasyGoPiGo3()

servo1 = gpg.init_servo(port='SERVO1')
servo2 = gpg.init_servo(port='SERVO2')


def servo_go():
	servo1.rotate_servo(96)
	servo2.rotate_servo(96)
	time.sleep(1)
	servo1.rotate_servo(60)
	servo2.rotate_servo(60)
	time.sleep(1)
	servo1.rotate_servo(140)
	servo2.rotate_servo(140)
	time.sleep(2)
	
servo_go()
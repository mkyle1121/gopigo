#!/usr/bin/env python

import easygopigo3 as easy
import time
from random import *
import pygame
import threading
import os
import signal

gpg = easy.EasyGoPiGo3() # declare main gpg object
sensor = gpg.init_distance_sensor() # declare distance sensor from main gpg
servo = gpg.init_servo(port='SERVO1') # declare servo object from main gpg
servo2 = gpg.init_servo(port='SERVO2')

servo.rotate_servo(96)
servo2.rotate_servo(96)

j=96
for i in range(25):
	print(j)
	j=j-1
	servo.rotate_servo(j)
	time.sleep(.05)
	#servo2.rotate_servo(i-=1)

time.sleep(1)
servo.rotate_servo(80)
servo2.rotate_servo(80)
time.sleep(1)
servo.rotate_servo(65)
servo2.rotate_servo(65)
time.sleep(1)
servo.rotate_servo(80)
servo2.rotate_servo(110)
time.sleep(1)
servo.rotate_servo(110)
servo2.rotate_servo(80)

servo2.rotate_servo(70)
time.sleep(1)
servo2.rotate_servo(110)
time.sleep(1)
servo2.rotate_servo(80)
time.sleep(1)
servo2.rotate_servo(110)
time.sleep(1)






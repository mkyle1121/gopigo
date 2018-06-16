#!/usr/bin/env python

import easygopigo3 as easy
import time


gpg = easy.EasyGoPiGo3()

servo = gpg.init_servo()

servo.rotate_servo(100)
time.sleep(.5)

servo.rotate_servo(10)
time.sleep(.5)
servo.rotate_servo(170)
time.sleep(.75)

servo.rotate_servo(100)


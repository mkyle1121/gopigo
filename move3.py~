#!/usr/bin/env python

import easygopigo3 as easy
import time

gpg = easy.EasyGoPiGo3()

gpg.forward()
time.sleep(1)
gpg.stop()

servo = gpg.init_servo()
servo.rotate_servo(100)
time.sleep(.5)
servo.rotate_servo(10)
time.sleep(.5)
servo.rotate_servo(170)
time.sleep(.75)
servo.rotate_servo(100)

gpg.backward()
time.sleep(1)
gpg.stop()
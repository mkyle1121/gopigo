#!/usr/bin/env python
from gopigo import *
import time




servo_pos=90
servo(servo_pos)
time.sleep(.5)


while True:


    servo_pos=10 #to the right
    servo(servo_pos)
    time.sleep(2)

    servo_pos=170 #to the left
    servo(servo_pos)
    time.sleep(2)




servo_pos=90
servo(servo_pos)

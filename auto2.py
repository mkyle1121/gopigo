#!/usr/bin/env python

import easygopigo3
import time
import threading

gpg = easygopigo3.EasyGoPiGo3()
SPEED = 150
gpg.set_speed(SPEED)
distance_sensor = gpg.init_distance_sensor()
servo1 = gpg.init_servo(port='SERVO1')
DISTANCE = 0
LOOK_LIST = []
servo_deg = 96

servo1.rotate_servo(180) # look left
time.sleep(1)
servo1.rotate_servo(20) # look right
time.sleep(1)
servo1.rotate_servo(96) # look center
time.sleep(1)

#################################################

while True: # constant while loop
	DISTANCE = distance_sensor.read_inches() # read distance sensor
	print('distance is '+str(DISTANCE)) # print the distance
	if DISTANCE >= 50: # check if less than 5 inches
		gpg.set_speed(1000)
		gpg.forward()
		print ('>50')
	elif DISTANCE >= 25:
		gpg.set_speed(500)
		gpg.forward()
		print ('<50')
	elif DISTANCE >= 10:
		gpg.set_speed(300)
		gpg.forward()
		print ('<25')
	elif DISTANCE > 5:
		gpg.set_speed(150)
		gpg.forward()
		print ('<10')
	elif DISTANCE <= 5:
		print ('<5')
		gpg.stop()
		time.sleep(2) # wait 2 seconds
		servo1.rotate_servo(96) # center servo
		servo_deg = 96
		while servo_deg <= 180: # check degrees all the way left
			servo1.rotate_servo(servo_deg) # rotate servo to new degrees
			DISTANCE = distance_sensor.read_inches() # read distance
			print (DISTANCE) # print distance
			LOOK_LIST.append(DISTANCE) # add distance to look list
			servo_deg += 4 # add degrees 
			print ('servo degree = '+str(servo_deg)) # print degrees
		for i in LOOK_LIST:
			print(i)
		turn_left = True
		j=LOOK_LIST[8]
		for i in LOOK_LIST[9:]:
			if i >= j or i > 10:
				print (str(i)+' >= '+str(j)+' or '+str(i)+' > 10')
				pass	
			else:
				print (str(i)+' '+str(j))
				print ('Something is in the way!')
				turn_left = False
				break	
			j = i
		LOOK_LIST = [] # reset list
		if turn_left == True:
			print('turning left')
			gpg.set_speed(300)
			gpg.turn_degrees(-90, blocking=True)
			servo1.rotate_servo(96)	
	else:
		pass
	




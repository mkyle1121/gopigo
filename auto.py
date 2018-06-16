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
servo = gpg.init_servo() # declare servo object from main gpg
pygame.mixer.init() # initialize the mixer for sound

SPEED = 200
gpg.set_speed(SPEED)  # default speed
servo.rotate_servo(96) # zero servo
DISTANCE = 24 # set distance limit for going forward in inches
FORWARD_TIME = 2 # set distance limit for max time to go forward

def GO_left_or_right():
	left_right_wait = randint(1,2)
	if left_right_wait == 1:
		GO_left()
	elif left_right_wait == 2:
		GO_right()

def GO_left():
	print ('Going Left!')
	GO_sound('MJ3.mp3')
	servo.rotate_servo(160)
	time.sleep(.5)
	gpg.turn_degrees(-90)
	time.sleep(.7)
	servo.rotate_servo(96)
	
def GO_right():
	print ('Going Right!')
	GO_sound('MJ4.mp3')
	servo.rotate_servo(10) # look left
	time.sleep(.5)
	gpg.turn_degrees(90) # turn left
	time.sleep(.7)
	servo.rotate_servo(96) # look straight
	
def GO_forward():
	while True:
		distance = sensor.read_inches() # read the inches from sensor
		if distance  >= DISTANCE: # forward test
			print ('Forward! '+(str(distance))) # print the distance
			GO_sound('MJ2.mp3')
			gpg.forward()
			GO_eyes()
			time.sleep(FORWARD_TIME) # only forward for 3 seconds
			gpg.stop() # stops!
			break # break after going forward for 3 seconds
		else:
			print ('Too Close, Stop!')
			gpg.stop()
			break
			
def GO_backward(): # go backward
	print ('Backward!')
	gpg.set_speed(100)
	GO_sound('MJ_BJ_2.mp3')
	gpg.backward()
	time.sleep(5)
	gpg.stop()
	gpg.set_speed(SPEED)
			
def GO_servo(): # fancy servo stuff, no important use
	print ('Servo Time!')
	GO_sound('MJ5.mp3')
	servo.rotate_servo(160)
	time.sleep(.5)
	servo.rotate_servo(10)	
	time.sleep(.5)
	servo.rotate_servo(96)
	time.sleep(.5)
	time.sleep(1) # let the music finish!
	
def GO_wait_random():
	time_wait = randint(1,5) # pick random time to wait
	print ('Waiting '+str(time_wait)+' seconds')
	time.sleep(time_wait) # wait that long
	
def GO_sound(song): # play a song in the local directory
	pygame.mixer.music.load('/home/pi/aaa_mikes_gopigo/sounds/'+song)
	pygame.mixer.music.play()
	
def GO_eyes(): # flash the eyes once
	gpg.set_eye_color((255,0,0))
	gpg.open_eyes()
	time.sleep(.1)
	gpg.set_eye_color((0,255,0))
	gpg.open_eyes()
	time.sleep(.1)
	gpg.set_eye_color((0,0,255))
	gpg.open_eyes()
	time.sleep(.1)
	gpg.close_eyes()
	
def GO_thread():  # menu thread for commands
	while True:
		command = input('Input command: ')
		if command == 'quit' or 'exit':
			servo.rotate_servo(96)
			gpg.stop()
			time.sleep(.5)
			os.kill(os.getpid(), signal.SIGINT) # kill the python process
	
#################### BOOT ###########################

print ('Booting!')
GO_sound('Robot_Boot.mp3')
time.sleep(1)
servo.rotate_servo(140)
time.sleep(.5)
servo.rotate_servo(70)
time.sleep(.5)
servo.rotate_servo(96)
gpg.forward()
time.sleep(.5)
gpg.backward()
time.sleep(.5)
gpg.stop()
time.sleep(.2) # to line up sound heh
GO_eyes()
print ('Done Booting!')

T1 = threading.Thread(target=GO_thread) # start main menu thread
T1.daemon=True
T1.start()
time.sleep(3) # time wait after booting!

	
#################### MAIN LOGIC #######################	
	
while True:	

	choice = randint(1,6) # pick a number !
	
	if choice == 1:
		GO_wait_random()
	elif choice == 2:
		GO_forward()	
	elif choice == 3:	
		GO_servo()
	elif choice == 4:
		GO_left()
	#elif choice == 5:
	#	GO_backward()
	elif choice == 6:
		GO_right()
		

#!/usr/bin/env python

import robot
import threading
import socket
import time

server = socket.gethostbyname('robot.themikekyle.com')
print (server)
state = False

while True:
	while state == False:		
		try:
			print ('Trying to contact server.')
			s = socket.socket()
			s.connect ((server, 8888))
		except ValueError:
			print ('something error')
		except socket.error:
			print ('Connection Refused')
			time.sleep (5)
		else:
			print ('Connected')
			state = True
			break

	print ('Waiting for data...')
	data = s.recv(2048)	
	if not data:
		s.close()
		state = False
	print (data.decode())
	if data == 'forward':
		print ('forward!')
		robot.forward()
	elif data == 'stop':
		print ('stop!')
		robot.stop()
	elif data == 'left':
		print ('left')
		robot.left()
	elif data == 'right':
		print ('right')
		robot.right()
	elif data == 'backward':
		print ('backward')
		robot.backward()
	elif data == 'servo left':
		print ('servo left')
		robot.servo_left()
	elif data == 'servo center':
		print ('servo center')
		robot.servo_center()
	elif data == 'servo right':
		print ('servo right')
		robot.servo_right()
	elif data == 'lights':
		print ('lights')
		robot.lights()
	elif data == 'blinkers':
		print ('blinkers')
		robot.blinkers()
	else:
		pass

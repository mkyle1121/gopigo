#!/usr/bin/env python

import robot
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import logging

def send_json(data):
	msg = {'action':data}
	msg = json.dumps(msg)
	return (msg)	

def action(client, userdata, message):	
	data = message.payload.decode()
	data = json.loads(data)
	data = data['action']
	print (data)
	if data == 'forward':
		print ('forward')
		robot.forward()
	elif data == 'stop':
		print ('stop')
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
	elif data == 'voltage':
		print('voltage')
		voltage = robot.voltage()
		voltage = send_json(voltage)
		myMQTT.publish('from_robot', voltage, 0)
	elif data == 'distance':
		print('distance')
		distance = robot.distance()
		distance = send_json(distance)
		myMQTT.publish('from_robot', distance, 0)
	else:
		pass

key_dir = '/home/pi/aaa_mikes_gopigo/keys/'

myMQTT = AWSIoTMQTTClient('Leonard')
myMQTT.configureEndpoint('a111amujev1y9r.iot.us-west-2.amazonaws.com', 8883)
myMQTT.configureCredentials(key_dir+'root-CA.crt', key_dir+'Leonard.private.key', key_dir+'Leonard.cert.pem')
myMQTT.configureOfflinePublishQueueing(-1)
myMQTT.configureDrainingFrequency(2)
myMQTT.configureConnectDisconnectTimeout(10)
myMQTT.connect()
myMQTT.subscribe('to_robot', 1, action)

logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

print('Waiting for data...')

while True:
	pass

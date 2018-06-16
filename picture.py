#!/usr/bin/env python

from picamera import PiCamera
from time import sleep
import boto3

camera = PiCamera()
camera.start_preview()
sleep(1)
camera.capture('/tmp/picture.jpg')
camera.stop_preview()

imageFile='/tmp/picture.jpg'
client=boto3.client('rekognition','us-west-2')
   
with open(imageFile, 'rb') as image:
    response = client.detect_labels(Image={'Bytes': image.read()})
print (response)
 
print('Detected labels in ' + imageFile)    
for label in response['Labels']:
    print (label['Name'] + ' : ' + str(label['Confidence']))
print('Done...')
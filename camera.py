#!/usr/bin/env python

from picamera.array import PiRGBArray # needs to be added so not hard dependency on numpy
from picamera import PiCamera
import time 
import cv2

camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

camera.capture(rawCapture, format='bgr') # capture and store image as rawcapture
image = rawCapture.array

cv2.imshow("Image", image)
cv2.waitKey(0)


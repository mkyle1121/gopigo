#!/usr/bin/env python

import easygopigo3 as easy
import time

gpg = easy.EasyGoPiGo3()


while True:
    #for a in range(200):
        #print a
    #gpg.set_eye_color((a,255-a,a))
    gpg.set_eye_color((255,0,0))
    gpg.open_eyes()
    time.sleep(.1)
    gpg.set_eye_color((0,255,0))
    gpg.open_eyes()
    time.sleep(.1)
    gpg.set_eye_color((0,0,255))
    gpg.open_eyes()
    time.sleep(.1)
        #time.sleep(.01)




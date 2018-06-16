#!/usr/bin/env python

import easygopigo3 as easy




gpg = easy.EasyGoPiGo3()

sensor = gpg.init_distance_sensor()


try:
    while True:
        dist = sensor.read_inches()
        print (str(dist)+' inches') 
except KeyboardInterrupt:
    pass

print ('here is the end')


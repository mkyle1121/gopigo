#!/usr/bin/env python

import easygopigo3 as easy
import time

gpg = easy.EasyGoPiGo3()

while  True:
    gpg.blinker_on(0)
    time.sleep(.1)
    gpg.blinker_off(0)
    gpg.blinker_on(1)
    time.sleep(.1)
    gpg.blinker_off(1)
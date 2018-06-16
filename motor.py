#!/usr/bin/env python

from __future__ import print_function
from __future__ import division

import gopigo3
import time

GPG = gopigo3.GoPiGo3()

GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, 10)
time.sleep(1)


#!/usr/bin/env python

import di_sensors.inertial_measurement_unit as IMU

imu = IMU.InertialMeasurementUnit()

mag   = imu.read_magnetometer()
gyro  = imu.read_gyroscope()
accel = imu.read_accelerometer()
euler = imu.read_euler()
temp  = imu.read_temperature()

print (mag, gyro, accel, euler, temp)

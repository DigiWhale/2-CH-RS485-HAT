#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial

TXDEN_1 = 27
TXDEN_2 = 22
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TXDEN_1, GPIO.OUT)
GPIO.setup(TXDEN_2, GPIO.OUT)
GPIO.output(TXDEN_1, GPIO.HIGH)
GPIO.output(TXDEN_2, GPIO.HIGH)
ser = serial.Serial("/dev/ttySC0", 115200, timeout=0.01)
total_distance = 0
total_time = 0
time_interval = 0.01

try:
    while(1):
        data = ser.read(1000000).decode("utf-8")
        total_time += time_interval
        if (data):
            speed =  len(data)/2.237
            distance = speed * time_interval
            total_distance += distance
            print(speed, "m/s", distance, "m")
            
except KeyboardInterrupt:    
    print('  Travelled ', round(total_distance, 4), 'm in ', round(total_time, 4), 's')
    exit()

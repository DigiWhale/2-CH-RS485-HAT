#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
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
data = ''
total_distance = 0
total_time = 0

try:
    while(1):
        data_t = ser.read(1000000).decode("utf-8")
        data += str(data_t)
        if(data):
            speed =  round(len(data)/2.237, 2)
            time_interval = 0.01
            distance = speed * time_interval
            total_distance += distance
            total_time += time_interval
            print(speed, "m/s", distance, "m")
            data = ''
            
except KeyboardInterrupt:    
    print(total_distance, "m", 'travelled')
    exit()

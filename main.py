#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial
import redis
import json
from datetime import datetime

r = redis.Redis(host="192.168.1.4", port=6379, db=0, password='Redis2019!')
TXDEN_1 = 27
TXDEN_2 = 22
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TXDEN_1, GPIO.OUT)
GPIO.setup(TXDEN_2, GPIO.OUT)
GPIO.output(TXDEN_1, GPIO.HIGH)
GPIO.output(TXDEN_2, GPIO.HIGH)
ser = serial.Serial("/dev/ttySC0", 256000, timeout=0.1)
total_distance = 0
total_time = 0
time_interval = 0.1
stopped = False

try:
    while(1):
        data = ser.read(1000000)
        total_time += time_interval
        if (data):
            stopped = False
            speed =  (len(data)/10)/2.237
            distance = speed * time_interval
            total_distance += distance
            print(speed, "m/s", distance, "m")
            r.hmset('doppler', {"speed": speed, "distance": distance, "total_distance": total_distance, "total_time": total_time})
        elif (stopped == False):
            stopped = True
            print("Stopped")
            r.hmset('doppler', {"speed": 0, "distance": 0, "total_distance": total_distance, "total_time": total_time})
            
except KeyboardInterrupt:    
    # print('  Travelled', round(total_distance, 4), 'm in', round(total_time, 4), 's')
    exit()

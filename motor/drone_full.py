# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

# pin: 11, 12, 15, 16
# BCM: 17, 18, 22, 23
front_l = 17
front_r = 18
back_l = 22
back_r = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(front_l, GPIO.OUT)
GPIO.setup(front_r, GPIO.OUT)
GPIO.setup(back_l, GPIO.OUT)
GPIO.setup(back_r, GPIO.OUT)

try:
    while (True):
        GPIO.output(front_l, GPIO.HIGH)
        GPIO.output(front_r, GPIO.HIGH)
        GPIO.output(back_l, GPIO.HIGH)
        GPIO.output(back_r, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(front_l, GPIO.LOW)
        GPIO.output(front_r, GPIO.LOW)
        GPIO.output(back_l, GPIO.LOW)
        GPIO.output(back_r, GPIO.LOW)
        time.sleep(2)
finally:
    print("Cleaning Up!")
    GPIO.cleanup()

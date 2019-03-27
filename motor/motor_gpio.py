# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

motor_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pin, GPIO.OUT)

try:
    while (True):
        GPIO.output(motor_pin, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(motor_pin, GPIO.LOW)
        time.sleep(2)
finally:
    print("Cleaning Up!")
    GPIO.cleanup()

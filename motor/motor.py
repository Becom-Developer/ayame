# -*- coding: utf-8 -*-
import wiringpi as pi
import time

motor_pin = 18

pi.wiringPiSetupGpio()
pi.pinMode( motor_pin, pi.OUTPUT)

try:
    while True:
        pi.digitalWrite(motor_pin, pi.HIGH)
        time.sleep(2)

        pi.digitalWrite(motor_pin, pi.LOW)
        time.sleep(2)
finally:
    print("Cleaning Up!")
    pi.serialClose(motor_pin)

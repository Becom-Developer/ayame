# -*- coding: utf-8 -*-
import wiringpi as pi
import time

motor_pin = 18

pi.wiringPiSetupGpio()
pi.pinMode( motor_pin, pi.OUTPUT)

pi.softPwmCreate( motor_pin, 0, 100)
pi.softPwmWrite( motor_pin, 0 )

try:
    while True:
        speed = 0
        while ( speed <= 100 ):
            pi.softPwmWrite( motor_pin, speed )
            time.sleep(0.3)
            speed = speed + 1

        pi.softPwmWrite( motor_pin, 0 )
        time.sleep(2)
finally:
    print("Cleaning Up!")
    pi.serialClose(motor_pin)

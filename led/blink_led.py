# -*- coding: utf-8 -*-
import wiringpi as pi
import time

led_pin = 18

pi.wiringPiSetupGpio()

pi.pinMode( led_pin, pi.output)

while True:
    pi.digitalWrite(led_pin, pi.LOW)
    time.sleep(1)

    pi.digitalWrite(led_pin, pi.HIGH)
    time.sleep(1)
finally:
    print("Cleaning Up!")
    GPIO.cleanup()


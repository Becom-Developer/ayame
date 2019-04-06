# -*- coding: utf-8 -*-
import wiringpi as pi
import time

# pin: 11, 12, 15, 16
# BCM: 17, 18, 22, 23
front_l = 17
front_r = 18
back_l = 22
back_r = 23

pi.wiringPiSetupGpio()
pi.pinMode( front_l, pi.OUTPUT)
pi.pinMode( front_r, pi.OUTPUT)
pi.pinMode( back_l, pi.OUTPUT)
pi.pinMode( back_r, pi.OUTPUT)

pi.softPwmCreate( front_l, 0, 100)
pi.softPwmWrite( front_l, 0 )

pi.softPwmCreate( front_r, 0, 100)
pi.softPwmWrite( front_r, 0 )

pi.softPwmCreate( back_l, 0, 100)
pi.softPwmWrite( back_l, 0 )

pi.softPwmCreate( back_r, 0, 100)
pi.softPwmWrite( back_r, 0 )

try:
    while True:
        speed = 90
        pi.softPwmWrite(front_l, speed)
        pi.softPwmWrite(front_r, speed)
        pi.softPwmWrite(back_l, speed)
        pi.softPwmWrite(back_r, speed)
        time.sleep(2)

        pi.softPwmWrite(front_l, 0)
        pi.softPwmWrite(front_r, 0)
        pi.softPwmWrite(back_l, 0)
        pi.softPwmWrite(back_r, 0)
        time.sleep(2)
finally:
    print("Cleaning Up!")
    pi.serialClose(front_l)
    pi.serialClose(front_r)
    pi.serialClose(back_l)
    pi.serialClose(back_r)

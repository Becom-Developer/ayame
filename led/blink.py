# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

# LED の点灯と消灯を繰り返す
# https://pinout.xyz/
# GPIO のピン番号の指定に注意
# Physical - ヘッダーのピンの物理位置に対応する番号
# BCM - Broadcomのピン番号

led_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while (True):
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(1)
finally:
    print("Cleaning Up!")
    GPIO.cleanup()

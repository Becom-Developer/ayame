import RPi.GPIO as GPIO
import time

# LED の点灯と消灯を繰り返す
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

try:
    while (True):
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(18, GPIO.LOW)
        time.sleep(1)
finally:
    print("Cleaning Up!")
    GPIO.cleanup()

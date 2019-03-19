import RPi.GPIO as GPIO
import time

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 50)
pwm_led.start(0)

try:
    while (True):
        for dc in range(0, 100, 5):
            pwm_led.ChangeDutyCycle(dc)
            time.sleep(0.05)
        for dc in range(100, 0, -5):
            pwm_led.ChangeDutyCycle(dc)
            time.sleep(0.05)
finally:
    print("Cleaning Up!")
    GPIO.cleanup()

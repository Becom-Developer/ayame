import RPi.GPIO as GPIO

# LED を任意の明るさで点灯
led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

try:
    while (True):
        duty_s = raw_input("Enter Brighness (0 to 100):")
        duty = int(duty_s)
        pwm_led.ChangeDutyCycle(duty)
finally:
    print("Cleaning Up!")
    GPIO.cleanup()

import RPi.GPIO as GPIO

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWN(led_pin, 500)
pwm_led.start(100)

try:
    while (True):
        duty_s = raw_input("Enter Brighness (0 to 100):")
        duty = int(duty_s)
        pwm_led.ChangeDutyCycle(duty)
finally:
    print("Cleaning Up!")
    GPIO.cleanup()

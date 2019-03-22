import RPi.GPIO as GPIO

# LED を一瞬だけ点灯
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)
GPIO.output(18, GPIO.LOW)
GPIO.cleanup()

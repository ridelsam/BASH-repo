

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.cleanup()

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while (1):
	GPIO.output(18, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(18, GPIO.LOW)
	#time.sleep(1)

	GPIO.output(23, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(23, GPIO.LOW)
	#time.sleep(1)

	GPIO.output(24, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(24, GPIO.LOW)
	#time.sleep(1)

#GPIO.cleanup()

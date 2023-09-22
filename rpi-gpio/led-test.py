
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.cleanup()


# pin assignment 
ecu0_fail = 18
ecu0_pass = 23
ecu1_fail = 24
ecu1_pass = 25
ecu2_fail = 8
ecu2_pass = 7
ecu3_fail = 1
ecu3_pass = 12


GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(ecu3_fail, GPIO.OUT)
GPIO.setup(ecu3_pass, GPIO.OUT)


# rolling lights test
while (1):
	GPIO.output(ecu0_fail, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(ecu0_fail, GPIO.LOW)
	#time.sleep(1)

	GPIO.output(ecu0_pass, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(ecu0_pass, GPIO.LOW)
	#time.sleep(1)

	GPIO.output(ecu1_fail, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(ecu1_fail, GPIO.LOW)
	#time.sleep(1)

	GPIO.output(ecu1_pass, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(ecu1_pass, GPIO.LOW)
	
	GPIO.output(ecu2_fail, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(ecu2_fail, GPIO.LOW)

	GPIO.output(ecu2_pass, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(ecu2_pass, GPIO.LOW)

	GPIO.output(ecu3_fail, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(ecu3_fail, GPIO.LOW)

	GPIO.output(ecu3_pass, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(ecu3_pass,GPIO.LOW)

#GPIO.cleanup()

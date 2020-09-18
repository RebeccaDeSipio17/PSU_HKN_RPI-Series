#!/usr/bin/python3

#import RPi.GPIO as GPIO
#import time

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11, GPIO.OUT)

#for i in range(5):
#	GPIO.output(11,True)
#	time.sleep(2)
#	GPIO.output(11,False)
#	time.sleep(.5)
#	GPIO.output(11,True)
#	time.sleep(1)
#	GPIO.output(11, False)
#	time.sleep(.1)

#GPIO.cleanup()

from gpiozero import LED
from time import sleep

led = LED(17)

while True:
	print('entered the while loop')
	led.on()
	sleep(1)
	led.off()
	sleep(1)

GPIO.cleanup()

#!/usr/bin/python

from gpiozero import *
from time import *

led = LED(17)

for i in range(5):
	led.on()
	sleep(1)
	led.off()
	sleep(1)

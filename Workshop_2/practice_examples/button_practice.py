#!/usr/bin/python

from gpiozero import *
from time import *

led = LED(17)
button = Button(18)
flag = 1 
# the flag variable is just a variable I created to run two different
# implementation. When "flag" is defined as equal to 1, it will fun the first
# if condition... if "flag" is defined as equal to 2, it runs the second
# if condition

if flag==1:
  while True:
    if button.is_pressed:
      led.on()
    else:
      led.off()

if flag==2:

  while True:
    if button.is_pressed==1:
      if led.is_active==True:
        led.off()
        sleep(.5)
      else:
        led.on()
        sleep(.5)

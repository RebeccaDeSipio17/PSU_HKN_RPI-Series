#!/usr/bin/python

# import libraries
from gpiozero import *
import time
import RPi.GPIO as GPIO
import numpy as np

flag = 0

GPIO.setmode(GPIO.BCM)

TRIG1 = 6
ECHO1 = 13

TRIG2 = 19
ECHO2 = 26

GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)

GPIO.output(TRIG1, False)
GPIO.output(TRIG2, False)

# define inputs/outputs
red1 = LED(14); red2 = LED(16); 
yellow1 = LED(15); yellow2 = LED(20); 
green1 = LED(18); green2 = LED(21);

sensor1_readings = []
sensor2_readings = []

# need to get the distance senesor continuously reading values
while True:
  GPIO.output(TRIG1, True)
  time.sleep(0.00001)
  GPIO.output(TRIG1, False)

  while (GPIO.input(ECHO1)==0):
    pulse_start1 = time.time()
  while (GPIO.input(ECHO1)==1):
    pulse_end1 = time.time()

  GPIO.output(TRIG2, True)
  time.sleep(0.00001)
  GPIO.output(TRIG2, False)

  while (GPIO.input(ECHO2)==0):
    pulse_start2 = time.time()
  while (GPIO.input(ECHO2)==1):
    pulse_end2 = time.time()

  pulse_duration1 = pulse_end1 - pulse_start1
  pulse_duration2 = pulse_end2 - pulse_start2

  distance1 = pulse_duration1 * 17150
  distance1 = round(distance1, 2)
  distance2 = pulse_duration2 * 17150
  distance2 = round(distance2, 2)

  #print("sensor 1", distance1)
  #print("sensor 2", distance2)

  time.sleep(.75) # collect measurements every half a second
  sensor1_readings = np.append(sensor1_readings,[distance1])
  sensor2_readings = np.append(sensor2_readings,[distance2])

  current_reading1 = len(sensor1_readings)
  current_reading2 = len(sensor2_readings)
  #print("length of array 1", sensor1_readings)
  #print("length of array 2", sensor2_readings)


  if (current_reading1 < 4) & (current_reading2 < 4):
  # print("not enough readings yet")
    continue
  elif (green1.is_active == False) & (green2.is_active == False):

  # turn the green light on if
  # a car arrives at either sensor

    if ((sensor1_readings[current_reading1-1]<=8) & (sensor1_readings[current_reading1-2]<=8) & (sensor1_readings[current_reading1-3]<=8) & (sensor1_readings[current_reading1-4]<=8)) | \
       ((sensor2_readings[current_reading2-1]<=8) & (sensor2_readings[current_reading2-2]<=8) & (sensor2_readings[current_reading2-3]<=8) & (sensor2_readings[current_reading2-4]<=8)):
      sensor1_readings = []
      sensor2_readings = []

      print("Activating Traffic Light System...\n")

      green1.on()
      red2.on()
      time.sleep(3)
      distance1 = 200; distance2 = 200;

  elif green1.is_active == True:
    # with the green light on, if the button 
    # is pressed again, transition to yellow,
    # and then red. Once the button is pressed 
    # a second time, switch back to green. Repeat.
    if (sensor1_readings[current_reading1-1]<=8) & (sensor1_readings[current_reading1-2]<=8) & (sensor1_readings[current_reading1-3]<=8) & (sensor1_readings[current_reading1-4]<=8):
      print("Car has arrived at traffic light 2. \nChanging system pattern")
      sensor1_readings = []
      sensor2_readings = []

      time.sleep(1.5)
      # set green light on 1 and red light on 2
      green1.off()
      time.sleep(.25)
      # change set 1 to change to yellow
      # keep set 2 set to red
      yellow1.on(); time.sleep(4)
      # change set 1 to red and set 2 will wait 1 sec until changing to green
      yellow1.off(); time.sleep(.25);
      red1.on();     time.sleep(2);
      red2.off() 
      green2.on()
      print("Green light. GO!\n")

  elif green2.is_active == True:
    # now if the A buton is pressed for set one...
    # we want to have set 2 change yellow then red
    # and set 1 will then change to green.
    if (sensor2_readings[current_reading2-1]<=8) & (sensor2_readings[current_reading2-2]<=8) & (sensor2_readings[current_reading2-3]<=8) & (sensor2_readings[current_reading2-4]<=8):
      print("Car has arrived at traffic light 1. \nChanging system pattern")
      sensor1_readngs = []
      sensor2_readings = []

      time.sleep(1.5)
      # set green light on 1 and red light on 2
      green2.off()
      time.sleep(.25)
      # change set 1 to change to yellow
      # keep set 2 set to red
      yellow2.on(); time.sleep(4)
      # change set 1 to red and set 2 will wait 1 sec until changing to green
      yellow2.off(); time.sleep(.25);
      red2.on();     time.sleep(2);
      red1.off()
      green1.on()
      print("Green light. GO!\n")


  if (current_reading1 > 15) & (current_reading2 > 15):
    print("No traffic!")
    break

  #print(current_reading1)
  #print(current_reading2)

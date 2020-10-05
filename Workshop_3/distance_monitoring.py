# import libraries
import RPi.GPIO as GPIO
import time

# set up the GPIO
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
perfect = 6
almost_there = 13
closer = 19
far_away = 26

GPIO.setup(TRIG,GPIO.OUT) # set TRIG as ouput - trigger the sensor
GPIO.setup(ECHO,GPIO.IN) # set ECHO as input - detect the ECHO voltage change
GPIO.setup(perfect,GPIO.OUT)
GPIO.setup(almost_there,GPIO.OUT)
GPIO.setup(closer,GPIO.OUT)
GPIO.setup(far_away,GPIO.OUT)

GPIO.output(perfect, GPIO.LOW)
GPIO.output(almost_there, GPIO.LOW)
GPIO.output(closer, GPIO.LOW)
GPIO.output(far_away, GPIO.LOW)


GPIO.output(TRIG,False) # set the trigger pin low

print("Distance Measurement in Progress")
time.sleep(2)

while True:
    # this sensor requires a 10us pulse to trigger the module and obtain an echo response
    # To create our trigger pulse, set trigger pin high for 10us then low again
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

# need to obtain the duration of a pulse
# this is the duration from the sensor to the object, and then back to the sensor
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

# now convert the time it takes to distance
# speed = distance / time 
# speed of sound = 343m/s
# since the recorded time is to the sensor and back, we need to divide time by 2. 
# 34300 = d / (t/2) --> 17150 * t = d
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    print("Distance: ",distance, "cm")
    time.sleep(.25)

    if distance > 200:
        break

    if (distance >= 20):
        GPIO.output(far_away,GPIO.HIGH)
        GPIO.output(perfect, GPIO.LOW)
        GPIO.output(almost_there, GPIO.LOW)
        GPIO.output(closer, GPIO.LOW)
    if (15 <= distance) & (distance < 20):
        GPIO.output(far_away, GPIO.HIGH)
        GPIO.output(closer, GPIO.HIGH)
        GPIO.output(perfect, GPIO.LOW)
        GPIO.output(almost_there, GPIO.LOW)
    if (10 <= distance) & (distance <= 15):
        GPIO.output(far_away, GPIO.HIGH)
        GPIO.output(closer, GPIO.HIGH)
        GPIO.output(almost_there, GPIO.HIGH)
        GPIO.output(perfect, GPIO.LOW)
    if (3 <= distance) & (distance <= 10):
        GPIO.output(far_away, GPIO.HIGH)
        GPIO.output(closer, GPIO.HIGH)
        GPIO.output(almost_there, GPIO.HIGH)
        GPIO.output(perfect, GPIO.HIGH)

GPIO.cleanup()


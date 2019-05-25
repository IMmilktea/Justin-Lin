#import pigpio
#import numpy as np
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import time
import board
import busio
import Adafruit_LSM303
import math

i2c = busio.I2C(board.SCL, board.SDA) # Get the data from LSM303
sensor = Adafruit_LSM303.LSM303(i2c)

STEP_PIN = 25 # choose GPIO 25 as our STEP GPIO pin
DIR_PIN = 21 # choose GPIO 21 as our DIR GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP_PIN, GPIO.OUT,initial=GPIO.LOW)  # set the GPIO 25 as GPIO OUT and initial to low
data = Adafruit_ADS1x15.ADS1115()

GAIN = 1  # GAIN = 1 means voltage between +/-4.096V
l = []  # create empty list
print('Get the sampling data From ADC')
print('ADC       x       y       heading angle'.format(*range(1)))
print('-' * 40)

q = ((data.read_adc(0, gain=GAIN))//132) # q is for the first position revise.
if (q) >0:                               # The reason using 132 is full step, 26400/132 =200= 360 degree
        for j in range(q):
            GPIO.output(STEP_PIN, 1)  # duty cycle is 50%, since High and low are half half.
            time.sleep(0.0025)
            GPIO.output(STEP_PIN, 0)
            time.sleep(0.0025)

while True:  # keeping get data until ctrl + C
    
    accel, mag= sensor.read()
    mag_x, mag_y, mag_x= mag
    heading = (math.atan2(mag_y, mag_x)*180)/math.pi # Calculate the angle of the vector y,x
    if heading < 0:
        heading += 360 # Normalize to 0-360
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(STEP_PIN, GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(DIR_PIN, GPIO.OUT)
    #GPIO.output(24,dire)

    values = [0]  # Read A0 channel values in a list

    for i in range(1):
        values[i] = data.read_adc(i, gain=GAIN)

    l.append(values[i])  # add the values[i] into list
    #print(values[i], angel, end='') # debug code
    print('| {0:>6}| {1:>6}|  {2:>6}|  {3:>6}|'.format(*values, mag_x, mag_y, heading))

    
    if len(l) >1: # r is for the currently position detect.
        r = ((l[len(l)-1] - l[len(l)-2])//132)
        #print(r)
        if r > 0:
            for n in range(r):
                GPIO.output(DIR_PIN, 0)
                GPIO.output(STEP_PIN, 1)
                time.sleep(0.0025)
                GPIO.output(STEP_PIN, 0)
                time.sleep(0.0025)
        else:
            for n in range(abs(r)):
                GPIO.output(DIR_PIN, 1)
                GPIO.output(STEP_PIN, 1)
                time.sleep(0.0025)
                GPIO.output(STEP_PIN, 0)
                time.sleep(0.0025)
    GPIO.cleanup()
    time.sleep(1)  # Time of getting data

   












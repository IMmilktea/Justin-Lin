import pigpio
import time
import matplotlib.pyplot as plt
import numpy as np
import Adafruit_ADS1x15
import RPi.GPIO as GPIO

LED_PIN = 23 # choose GPIO 23 as our GPIO pin
PWM_FREQ = 200 # PWM setting on 200 

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT) # set the GPIO 23 as GPIO OUT
pwm = GPIO.PWM(LED_PIN, PWM_FREQ) # import the PWM function
pwm.start(0)

data = Adafruit_ADS1x15.ADS1115()

GAIN = 1 # GAIN = 1 means voltage between +/-4.096V
l =[] # create empty list
print('et the sampling data From ADC')
print('ADC channel A0'.format(*range(1)))
print('-' * 15)
while True: # keeping get data until ctrl + C
    
    values = [0] # Read A0 channel values in a list
    
    for i in range(1):
        
        values[i] = data.read_adc(i, gain=GAIN)
        
    l.append(values[i]) #add the values[i] into list
    print('| {0:>6}|'.format(*values))
    pwm.ChangeDutyCycle(100*q/26400) # 26400 is the biggest data at 3.3V
    
    time.sleep(0.5) # Time of getting data







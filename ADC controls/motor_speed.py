#import numpy as np
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import board
import busio
import Adafruit_LSM303
import time

i2c = busio.I2C(board.SCL, board.SDA) # Get the data from LSM303
sensor = Adafruit_LSM303.LSM303(i2c)

Motor_PIN = 25 # choose GPIO 25 as our GPIO pin
PWM_FREQ = 200 # PWM setting on 200 
GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor_PIN, GPIO.OUT) # set the GPIO 25 as GPIO OUT
pwm = GPIO.PWM(Motor_PIN, PWM_FREQ) # import the PWM function
pwm.start(0) # PWM start

data = Adafruit_ADS1x15.ADS1115()

GAIN = 1 # GAIN = 1 means voltage between +/-4.096V
l =[] # create empty list
print('et the sampling data From ADC')
print('ADC     x-accel   y-accel'.format(*range(1)))
print('-' * 15)
while True: # keeping get data until ctrl + C
    accel, mag= sensor.read() # Get the mag and accel data
    accel_x, accel_y, accel_z= accel
    
    values = [0] # Read A0 channel values in a list
    for i in range(1):
        values[i] = data.read_adc(i, gain=GAIN)
        
    l.append(values[i]) #add the values[i] into list
    print('| {0:>6}| {1:>6}| {2:>6}|'.format(*values, accel_x, accel_y))
    #pwm.ChangeDutyCycle(50) # test code
    pwm.ChangeDutyCycle(int((values[i]/264))) # 26400 is the biggest data at 3.3v, 100 is max value for dutycycle
    pwm.ChangeFrequency(int((values[i]/264))*2+1) # +1 is because of frequency can't be 0
    #r = int(((values[i]/264))) # debug code
    #print(r) # debug code
    time.sleep(0.5) # Time of getting data
GPIO.cleanup()




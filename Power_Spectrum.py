import time
import matplotlib.pyplot as plt
import numpy as np
import Adafruit_ADS1x15
from scipy.fftpack import fft,ifft

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1 # GAIN = 1 means voltage between +/-4.096V
l =[] # create empty list
print('Get the sampling data From ADC')
print('| {0:>6}|'.format(*range(1)))
print('-' * 15)

for j in range(500): # Main loop.
    
    values = [0] # Read A0 channel values in a list
    for i in range(1):
        
        values[i] = adc.read_adc(i, gain=GAIN)
   
    l.append(values[i]) #add the values[i] into list
    
    print('| {0:>6}|'.format(*values))
    time.sleep(0.002) # Time of getting data

lf = fft(l) # FFT l list
lf1 = abs(lf) # Power spectrum lf
plt.title('Power spectrum result')
plt.xlabel('number of samples')
plt.ylabel('value of power spectrum')
plt.plot(lf1)
plt.draw()
plt.pause(10)
plt.savefig("FFT-figure.jpg")
plt.close()
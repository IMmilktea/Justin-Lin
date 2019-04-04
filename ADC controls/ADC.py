import time
import matplotlib.pyplot as plt
import numpy as np
import Adafruit_ADS1x15

data = Adafruit_ADS1x15.ADS1115()

GAIN = 1 # GAIN = 1 means voltage between +/-4.096V
l =[] # create empty list
print('Get the sampling data from ADC')
print('ADC channel A0'.format(*range(1)))
print('-' * 15)
N = 10 # Take the N numbers of sample data from ADC
for j in range(N):  # Main loop.
    
    values = [0] # Read A0 channel values in a list
    for i in range(1):
        
        values[i] = data.read_adc(i, gain=GAIN) # Read the specified ADC channel using the previously set gain value.
   
    
    l.append(values[i]) #add the values[i] into list
    
    print('| {0:>6}|'.format(*values))    
    time.sleep(15) # Time of getting data


print(l)
l2=range(N)

plt.title('Data smaple result')
plt.xlabel('number of samples')
plt.ylabel('value of samples')
plt.plot(l)
plt.plot(l2, l,'ro')
plt.draw() 
plt.pause(10)
plt.savefig("Data-figure.jpg")  #save picture
plt.close()   #close picture

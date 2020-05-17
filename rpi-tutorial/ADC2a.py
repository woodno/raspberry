# ADC2a.py

from ADS1x15 import ADS1115
from py7seg import Py7Seg # xxx
import time

adc = ADS1115()
channel = 0
gain = 1
ps = Py7Seg() # xxx
t = 0
while True:
    data = adc.read_adc(channel, gain)
    print t, "s:", data
    ps.showText("%4d" %data) # xxx
    t += 0.1
    time.sleep(0.1)

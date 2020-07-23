# Infrared2.py
# GP2Y0A21YK sensor with PCF8591 ADC

import smbus
import time
from py7seg import Py7Seg # xxx

bus = smbus.SMBus(1)  # RPi revision 2 (0 for revision 1)
i2c_address = 0x48
ps = Py7Seg() # xxx
# u = mx + b, x = 1/d
m = 19.8
b = 0.228
while True:
    data = bus.read_byte_data(i2c_address, 0) # use CH0
    u = data / 255 * 5
    d = int(m / (u - b))
    print "d =" ,d, "cm"
    ps.showText("%4d" %d) # xxx
    time.sleep(0.1)

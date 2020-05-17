 # ADC1a.py
# PCF8591, read values from analog input 0

import smbus
import time
#from py7seg import Py7Seg # xxx

bus = smbus.SMBus(1)  # RPi revision 2 (0 for revision 1)
i2c_address = 0x48
control_byte = 0x00                                                                                                                                                                                                                                                                                           # to read channel 0
#ps = Py7Seg() # xxx
t = 0
while True:
    data = bus.read_byte_data(i2c_address, control_byte)
    print t, "s:", data
#    ps.showText("%4d" %data) # xxx
    t += 0.1
    time.sleep(0.1)

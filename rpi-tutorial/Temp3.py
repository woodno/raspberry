# Temp3.py
# Temperature sensor MCP9808

import smbus
import time

i2c_address        = 0x18
temp_register      = 0x05

def readTemp():
    v = bus.read_word_data(i2c_address, temp_register)
    hiByte = v & 0x00FF  # SMBus with reversed byte order
    loByte = (v >> 8) & 0x00FF
    hiByte = hiByte  & 0x1F # clear flag bit
    if hiByte & 0x10 == 0x10:  # temp < 0
        hiByte = hiByte & 0x0F  # clear sign
        temp = 256 - hiByte * 16 + loByte / 16.0 # scale
    else:
        temp = hiByte * 16 + loByte / 16.0 # scale
    return round(temp, 1)

print "starting..."
bus = smbus.SMBus(1) 
while True:
    t = readTemp()
    print "T =", t, "centigrades"  
    time.sleep(1)


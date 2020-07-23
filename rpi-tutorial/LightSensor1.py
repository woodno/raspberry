# LightSensor.py
# Light barrier with LDR sensor

import smbus
import time

TRIGGER_LEVEL = 300 # user selectable

def readData(port = 0):
    if port == 0:
        adc_address = 0x48
    elif port == 1:    
        adc_address = 0x4D
    rd = bus.read_word_data(adc_address, 0)
    data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
    data = data >> 2
    return data

print "starting..."
bus = smbus.SMBus(1) 

state = "DARK"
while True:
    v = readData(1)  # adapt to your ADC (0 or 1)
    if v >= TRIGGER_LEVEL and state == "DARK":
       state = "BRIGHT"
       print "BRIGHT event"
    if v < TRIGGER_LEVEL and state == "BRIGHT":
       state = "DARK"
       print "DARK event"



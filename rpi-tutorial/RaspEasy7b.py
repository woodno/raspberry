# RaspEasy7b.py
# Read ADC and show on Oled or 7-segment display

import smbus
import time
from OLED1306 import OLED1306
#from pytell import PyTell

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
oled = OLED1306()
oled.setFontSize(50)
#pyTell = PyTell()

bus = smbus.SMBus(1) 
while True:
    v = readData()
    oled.setText(str(v))
#    pyTell.showText("%4d" %v)
    time.sleep(1)


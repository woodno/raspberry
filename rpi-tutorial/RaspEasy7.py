# RaspEasy7.py
# Read ADC0 or ADC1 and write value to stdout

import smbus
import time

print "starting..."
bus = smbus.SMBus(1) 
adc_address = 0x48  # ADC0
# adc_address = 0x4D  # ADC 1

while True:
    # Reads word (16 bits) as int
    rd = bus.read_word_data(adc_address, 0)
    # Exchanges high and low bytes
    data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
    # Ignores two least significiant bits
    data = data >> 2
    print "data:", data
    time.sleep(1)


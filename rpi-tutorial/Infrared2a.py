# Infrared2.py
# GP2Y0A21YK sensor with PCF8591 ADC

import smbus
from py7seg import Py7Seg # xxx
from Beeper import Beeper
import time

P_BUZZER = 22
beeper = Beeper(P_BUZZER)
bus = smbus.SMBus(1)  # RPi revision 2 (0 for revision 1)
i2c_address = 0x48
ps = Py7Seg() # xxx

# u = mx + b, x = 1/d
m = 19.8
b = 0.228
beeper.start(0.05, 0.2, 3, True) # to say we are ready
beeper.start(0, 0)
while True:
    data = bus.read_byte_data(i2c_address, 0) # use CH0
    u = data / 255.0 * 5
    d = int(m / (u - b))
    print "d =" ,d, "cm"
    if d > 0 and d < 50:
        ps.showText("%4d" %d) # xxx
    else:
        ps.showText("----") # xxx
    if d > 0 and d < 50:
        beeper.setOnOffTime(0.05, 0.01 * d)
    else:
        beeper.setOnTime(0)
    time.sleep(0.1)

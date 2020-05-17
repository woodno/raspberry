# ADC3b.py

import smbus
import time
from py7seg import Py7Seg # xxx
 
class MCP3021:
    VINmax = 3.3
    bus = smbus.SMBus(1)
    
    def __init__(self, address = 0x4D):
        self.address = address
    
    def setVINmax(self, v):
        self.VINmax = v
    
    def readRaw(self):
        # Reads word (16 bits) as int
        rd = self.bus.read_word_data(self.address, 0)
        # Exchanges high and low bytes
        data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
        # Ignores two least significiant bits
        return data >> 2
    
    def getValue(self):
        return float(self.VINmax) * self.readRaw() / 1023.0

adc = MCP3021()
ps = Py7Seg() # xxx
t = 0
while True:
    v = adc.getValue()
    print t, "s:", w
    w = "%4.3f" %v
    ps.showText(w[0] + w[2] + w[3] + w[4], dp = [0, 0, 1]) # xxx
    t += 0.1
    time.sleep(0.1)
# Servo2.py
# Two servo motors driven by PCA9685 chip

from smbus import SMBus
from PCA9685 import PWM
import time

i2c_address = 0x40
fPWM = 50
channel = 0
a = 8.5
b = 2

def setup():
    global pwm
    bus = SMBus(1) # Raspberry Pi revision 2
    pwm = PWM(bus, i2c_address)
    pwm.setFreq(fPWM)

def setDirection(direction):
    duty = a / 180 * direction + b
    pwm.setDuty(channel, duty)
    print "direction =", direction, "-> duty =", duty
    time.sleep(0.5) # allow to settle
   
print "starting"
setup()
for direction in range(0, 181, 10):
    setDirection(direction)
direction = 0    
setDirection(0)    
print "done"
  

# Infrared1.py
# using the PCF8591 ADC

import smbus
import time
import RPi.GPIO as GPIO


P_LED = 22
TRIGGER_LEVEL = 25
DT = 0.2

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_LED, GPIO.OUT)

def beep(n):
    for i in range(n):
        GPIO.output(P_LED, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(P_LED, GPIO.LOW)
        time.sleep(0.05)

bus = smbus.SMBus(1)  # RPi revision 2 (0 for revision 1)
i2c_address = 0x48
setup()
beep(3) # to say we are ready
while True:
    data = bus.read_byte_data(i2c_address, 0) # read ch0
    if data > TRIGGER_LEVEL:
        beep(2)
    time.sleep(DT)

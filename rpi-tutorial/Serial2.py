# Serial2.py

import serial
import time

port = "/dev/ttyAMA0"  # Raspberry Pi 2
#port = "/dev/ttyS0"    # Raspberry Pi 3

ser = serial.Serial(port, baudrate = 1200)
print "starting"
while True:
    time.sleep(1)
    ser.write("A")
    nbChars = ser.inWaiting()
    if nbChars > 0:
        data = ser.read(nbChars)
        print data

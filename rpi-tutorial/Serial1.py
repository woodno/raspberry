# Serial1.py

import serial
import time

port = "/dev/ttyAMA0"  # Raspberry Pi 2
#port = "/dev/ttyS0"    # Raspberry Pi 3

def readLine(port):
    s = ""
    while True:
        ch = port.read()
        s += ch
        if ch == '\r':
            return s

ser = serial.Serial(port, baudrate = 1200)
print "starting"
while True:
    time.sleep(1)
    print "sending synch"
    ser.write("A")
    rcv = readLine(ser)
    print "received:", rcv

# DataInsert2.py

import serial
import time, sys
import datetime
from SIM800Modem import *
import random

APN = "gprs.swisscom.ch"
HOST = "www.aplu.dx.am"
PORT = 80

SERIAL_PORT = "/dev/ttyAMA0"  # Raspberry Pi 2
#SERIAL_PORT = "/dev/ttyS0"    # Raspberry Pi 3

print "Resetting modem..."
resetModem()
ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)
if not isReady(ser):
    print "Modem not ready."
    sys.exit(0)

print "Connecting to GSM net..."
connectGSM(ser, APN)
while True:
    startTime = time.time()
    t = datetime.datetime.now()
    x = str(t)
    x = x.replace(" ", "%20") # don't use space in url
    y = random.randint(1, 100)
    print "data:", x, y
    print "Sending HTTP request..."
    reply = connectTCP(ser, HOST, PORT)
    if "CONNECT OK" not in reply:
        print "Connection failed"
        sys.exit(0)
    sendHTTPRequest(ser, HOST, "/insert.php?x=" + x + "&y=" + str(y)) 
    print "Closing. Waiting for next transfer"
    closeTCP(ser)
    isRunning = True
    while time.time() - startTime < 60:
      time.sleep(0.1)

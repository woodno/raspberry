# SIMClient.py

import serial
import time, sys
from SIM800Modem import *
import RPi.GPIO as GPIO

APN = "gprs.swisscom.ch"
#HOST = "5.149.19.125"
HOST = "raspibrick.zapto.org"
PORT = 5000
SERIAL_PORT = "/dev/ttyAMA0"  # Raspberry Pi 2
#SERIAL_PORT = "/dev/ttyS0"    # Raspberry Pi 3
P_BUTTON = 24 # adapt to your wiring

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN, GPIO.PUD_UP)

setup()
print "Resetting modem..."
resetModem()
ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)
if not isReady(ser):
    print "Modem not ready."
    sys.exit(0)
    
print "Connecting to GSM net..."
connectGSM(ser, APN)

print "Connecting to TCP server..."
reply = connectTCP(ser, HOST, PORT)
if "CONNECT OK" not in reply:
    print "Connection failed"
    sys.exit(0)

print "Connection established. Sending data..."
while True:
    if GPIO.input(P_BUTTON) == GPIO.LOW:
        msg = "Button pressed"
    else:
        msg = "Button released"
    k = len(msg) # do not exceed value returned by AT+CIPSEND? (max 1460)
    ser.write("AT+CIPSEND=" + str(k) +"\r") # fixed length sending
    time.sleep(1) # wait for prompt
    ser.write(msg)
    time.sleep(2)

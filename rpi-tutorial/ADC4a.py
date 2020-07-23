# ADC4a.py

import RPi.GPIO as GPIO
import time
from py7seg import Py7Seg # xxx

SPI_CLK = 23
SPI_MISO = 21
SPI_MOSI = 19
SPI_CS = 24

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SPI_MOSI, GPIO.OUT)
    GPIO.setup(SPI_MISO, GPIO.IN)
    GPIO.setup(SPI_CLK, GPIO.OUT)
    GPIO.setup(SPI_CS, GPIO.OUT, initial = GPIO.HIGH)

def readADC(channel):
    LOW = GPIO.LOW
    HIGH = GPIO.HIGH

    if channel > 7 or channel < 0: # illegal channel
        return -1

    GPIO.output(SPI_CLK, LOW) # Start with clock low
    GPIO.output(SPI_CS, LOW)  # Enable chip

    # Send command
    control = channel # control register
    control |= 0b00011000  # Start bit at b4,  
                           # Single-ended bit at b3
                           # Channel number (b2, b1, b0)
    for i in range(5):  # Send bit pattern starting from bit b4
        if control & 0x10:  # Check bit b4
            GPIO.output(SPI_MOSI, HIGH)
        else:
            GPIO.output(SPI_MOSI, LOW)
        control <<= 1 # Shift left
        GPIO.output(SPI_CLK, HIGH) # Clock pulse
        GPIO.output(SPI_CLK, LOW)

    # Get reply
    data = 0
    for i in range(11):  # Read 11 bits and insert at right
        GPIO.output(SPI_CLK, HIGH)  # Clock pulse
        GPIO.output(SPI_CLK, LOW)
        data <<= 1  # Shift left, LSB = 0
        if GPIO.input(SPI_MISO): # If high, LSB = 1,
            data |= 0x1

    GPIO.output(SPI_CS, HIGH) # Disable chip
    return data

setup()
channel = 0
ps = Py7Seg() # xxx
t = 0
while True:
    data = readADC(channel)
    print t, "s:", data
    ps.showText("%4d" %data) # xxx
    t += 0.1
    time.sleep(0.1)
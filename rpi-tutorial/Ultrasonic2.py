 # Ultrasonic2.py
 # Show distance on Oled or 7-segment display

import RPi.GPIO as GPIO
import time
from OLED1306 import OLED1306
#from pytell import PyTell

P_ESCAPE = 12 # Button A
P_TRIGGER = 15
P_ECHO = 16

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_TRIGGER, GPIO.OUT)
    GPIO.setup(P_ECHO, GPIO.IN)
    GPIO.setup(P_ESCAPE, GPIO.IN)

def getDistance():        
    # Send max 10 us trigger pulse
    GPIO.output(P_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(P_TRIGGER, GPIO.LOW)

    start = time.time()
    end = time.time()
    
    # Wait for HIGH signal
    while GPIO.input(P_ECHO) == GPIO.LOW:
        start = time.time()
    # Wait for LOW signal
    while GPIO.input(P_ECHO) == GPIO.HIGH:
        end = time.time()
    elapsed = end - start
    distance =  34300 * elapsed / 2.0
    # round to 2 decimals
    distance = int(distance * 100 + 0.5) / 100.0
    return distance

print "starting..."
oled = OLED1306()
oled.setFontSize(50)
#pyTell = PyTell()
setup()
while GPIO.input(P_ESCAPE) == GPIO.LOW:
    d = getDistance()
    oled.setText(str(d))
#    pyTell.showText("%4d" %d)
    time.sleep(1)
GPIO.cleanup()
oled.setText("done")
# pyTell.showText("done")
    
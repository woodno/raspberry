# LED2.py

import RPi.GPIO as GPIO
import time
P_LED = 7 # adapt to your wiring

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_LED, GPIO.OUT)

print "blinking now"
setup()
while True:
    GPIO.output(P_LED, GPIO.HIGH)
    print "on"
    time.sleep(0.1)
    GPIO.output(P_LED, GPIO.LOW)
    print "off"
    time.sleep(0.1)

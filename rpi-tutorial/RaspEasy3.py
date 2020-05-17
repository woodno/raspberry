# RaspEasy3.py
# LED switcher

import RPi.GPIO as GPIO
import time

P_BUTTON = 12 # Button A
P_LED = 7 # LED A

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN)
    GPIO.setup(P_LED, GPIO.OUT)
    GPIO.output(P_LED, GPIO.LOW) # Turn off LED

print "starting..."
setup()
isLedOn = False
isButtonPressed = False
while True:
    if GPIO.input(P_BUTTON) == GPIO.HIGH and not isButtonPressed:
        isButtonPressed = True
        if isLedOn:
            isLedOn = False
            GPIO.output(P_LED, GPIO.LOW)
        else:
            isLedOn = True
            GPIO.output(P_LED, GPIO.HIGH)
        time.sleep(0.1)
    elif GPIO.input(P_BUTTON) == GPIO.LOW and isButtonPressed:
        isButtonPressed = False
        time.sleep(0.1)
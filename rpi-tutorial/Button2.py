# Button2.py

import RPi.GPIO as GPIO
import time

P_BUTTON = 15 # adapt to your wiring
P_LED = 7     # adapt to your wiring

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(P_LED, GPIO.OUT)
    
setup()
isLedOn = False
isButtonReady = True
while True:
    if isButtonReady and GPIO.input(P_BUTTON) == GPIO.LOW:  # pressed
        isButtonReady = False
        if not isLedOn:
            isLedOn = True
            GPIO.output(P_LED, GPIO.HIGH)
        else:
            isLedOn = False
            GPIO.output(P_LED, GPIO.LOW)
    if GPIO.input(P_BUTTON) == GPIO.HIGH:  # released
        isButtonReady = True
    time.sleep(0.01)  # remove this line to experience bouncing 


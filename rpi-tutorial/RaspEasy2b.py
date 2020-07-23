# RaspEasy2b.py
# Button counter, 3rd attempt

import RPi.GPIO as GPIO
import time

P_BUTTON = 12 # Button A

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN)

print "starting..."
setup()
count = 0
isButtonPressed = False
while True:
    if GPIO.input(P_BUTTON) == GPIO.HIGH and not isButtonPressed:
        isButtonPressed = True
        count += 1
        print count
        time.sleep(0.1)
    elif GPIO.input(P_BUTTON) == GPIO.LOW and isButtonPressed:
        isButtonPressed = False
        time.sleep(0.1)
# RaspEasy2a.py
# Button counter, 2nd attempt

import RPi.GPIO as GPIO

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
    elif GPIO.input(P_BUTTON) == GPIO.LOW and isButtonPressed:
        isButtonPressed = False

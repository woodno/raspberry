# RaspEasy2.py
# Button counter, 1st attempt

import RPi.GPIO as GPIO

P_BUTTON = 12 # Button A

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN)

print "starting..."
setup()
count = 0
while True:
    if GPIO.input(P_BUTTON) == GPIO.HIGH:
        count += 1
        print count

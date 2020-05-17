# RaspEasy1.py
# Button press/release to switch on/off LED

import RPi.GPIO as GPIO

P_BUTTON = 12 # Button A
#P_BUTTON = 13 # Button B
P_LED = 7 # LED A
#P_LED = 11 # LED B

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN)
    GPIO.setup(P_LED, GPIO.OUT)

print "starting..."
setup()
while True:
    if GPIO.input(P_BUTTON) == GPIO.HIGH:
        GPIO.output(P_LED, GPIO.HIGH)
    else:
        GPIO.output(P_LED, GPIO.LOW)

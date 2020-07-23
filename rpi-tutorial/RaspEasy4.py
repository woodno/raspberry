# RaspEasy4.py
# Start/Stop, Terminate

import RPi.GPIO as GPIO
import time

RUN_BUTTON = 12 # Button A
EXIT_BUTTON = 13 # Button B

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RUN_BUTTON, GPIO.IN)
    GPIO.setup(EXIT_BUTTON, GPIO.IN)

setup()
count = 0
isCounting = False
isRunButtonPressed = False
print "Stopped"
isExiting = False
while not isExiting:
    if GPIO.input(RUN_BUTTON) == GPIO.HIGH and not isRunButtonPressed:
        isRunButtonPressed = True
        if not isCounting:
            isCounting = True
            print "Counting..."
        else:
            isCounting = False
            print "Stopped"
        time.sleep(0.1)
    elif GPIO.input(RUN_BUTTON) == GPIO.LOW and isRunButtonPressed:
        isRunButtonPressed = False
        time.sleep(0.1)

    if isCounting:
        count += 1
        print count
        time.sleep(0.01)

    if GPIO.input(EXIT_BUTTON) == GPIO.HIGH:
        isExiting = True
 
GPIO.cleanup()        
print "Programm terminated"
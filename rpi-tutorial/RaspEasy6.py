# RaspEasy6.py

import RPi.GPIO as GPIO
import time

COUNT_BUTTON = 12 # Button A
EXIT_BUTTON = 13 # Button B

def onCountButtonEvent(channel):
    global count, btnReady
    if btnReady and GPIO.input(COUNT_BUTTON) == GPIO.HIGH:
        btnReady = False
        count += 1
    else:
        btnReady = True
    time.sleep(0.1)    

def onExitButtonEvent(channel):
    global isExiting
    isExiting = True

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(COUNT_BUTTON, GPIO.IN)
    GPIO.setup(EXIT_BUTTON, GPIO.IN)
    GPIO.add_event_detect(COUNT_BUTTON, GPIO.BOTH, onCountButtonEvent)
    GPIO.add_event_detect(EXIT_BUTTON, GPIO.BOTH, onExitButtonEvent)

setup()
btnReady = True
count = 0
oldCount = 0
print "starting..."
isExiting = False
while not isExiting:
    if count != oldCount:
        oldCount = count
        print count
    time.sleep(0.001)

GPIO.cleanup()        
print "Programm terminated"


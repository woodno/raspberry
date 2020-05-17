# RaspEasyAppendix1.py
# Start/Stop, Counting worker thread

import RPi.GPIO as GPIO
import time
from threading import Thread

RUN_BUTTON = 12 # Button A
EXIT_BUTTON = 13 # Button B

class WorkerThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.isAlive = True
        self.isHold = True
        self.start()
        
    def run(self):
        count = 0
        while self.isAlive:
            if self.isHold:
                time.sleep(0.1)
            else: 
                count += 1
                print count
                time.sleep(0.01)

    def kill(self):
        self.isAlive = False

    def hold(self):
        self.isHold = True

    def resume(self):
        self.isHold = False
                                        
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RUN_BUTTON, GPIO.IN)
    GPIO.setup(EXIT_BUTTON, GPIO.IN)

setup()
isPaused = True
isRunButtonPressed = False
print "Stopped"
isExiting = False
worker = WorkerThread()
while not isExiting:
    if GPIO.input(RUN_BUTTON) == GPIO.HIGH and not isRunButtonPressed:
        isRunButtonPressed = True
        if isPaused:    
            isPaused = False
            worker.resume()
            print "Working..."
        else:
            isPaused = True
            worker.hold()
            print "Paused"
    elif GPIO.input(RUN_BUTTON) == GPIO.LOW and isRunButtonPressed:
        isRunButtonPressed = False

    if GPIO.input(EXIT_BUTTON) == GPIO.HIGH:
        isExiting = True

    time.sleep(0.1)

worker.kill()        
GPIO.cleanup() 
print "Programm terminated"
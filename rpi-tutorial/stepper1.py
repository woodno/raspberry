# Stepper1.py

import RPi.GPIO as GPIO
import time

P_A1 = 8  # adapt to your wiring
P_A2 = 10 # ditto
P_B1 = 11 # ditto
P_B2 = 13 # ditto
delay = 0.005 # time to settle

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_A1, GPIO.OUT)
    GPIO.setup(P_A2, GPIO.OUT)
    GPIO.setup(P_B1, GPIO.OUT)
    GPIO.setup(P_B2, GPIO.OUT)

def forwardStep():
    setStepper(1, 0, 1, 0)
    setStepper(0, 1, 1, 0)
    setStepper(0, 1, 0, 1)
    setStepper(1, 0, 0, 1)

def backwardStep():
    setStepper(1, 0, 0, 1)
    setStepper(0, 1, 0, 1)
    setStepper(0, 1, 1, 0)
    setStepper(1, 0, 1, 0)
  
def setStepper(in1, in2, in3, in4):
    GPIO.output(P_A1, in1)
    GPIO.output(P_A2, in2)
    GPIO.output(P_B1, in3)
    GPIO.output(P_B2, in4)
    time.sleep(delay)

setup()
# 512 steps for 360 degrees, adapt to your motor
while True:
    print "forward"
    for i in range(256):
        forwardStep() 
    print "backward"
    for i in range(256):
        backwardStep() 

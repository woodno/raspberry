# LED1.py 

import RPi.GPIO as GPIO
import time
P_LED = 40 # adapt to your wiring

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_LED, GPIO.OUT)

def beep(n):
    for i in range(n):
        GPIO.output(P_LED, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(P_LED, GPIO.LOW)
        time.sleep(0.1)

print "beeping now"
setup()
beep(3)
GPIO.cleanup()
print "done"

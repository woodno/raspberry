# Ultrasonic1.py
# Using HC-SR04 ultrasonic module

import RPi.GPIO as GPIO
import time

P_ESCAPE = 12 # Button A
P_TRIGGER = 15
P_ECHO = 16

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_TRIGGER, GPIO.OUT)
    GPIO.setup(P_ECHO, GPIO.IN)
    GPIO.setup(P_ESCAPE, GPIO.IN)

def getDistance():        
    # Send max 10 us trigger pulse
    GPIO.output(P_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(P_TRIGGER, GPIO.LOW)

    start = time.time()
    end = time.time()
    
    # Wait for HIGH signal
    while GPIO.input(P_ECHO) == GPIO.LOW:
        start = time.time()
    # Wait for LOW signal
    while GPIO.input(P_ECHO) == GPIO.HIGH:
        end = time.time()
    elapsed = end - start
    distance =  34300 * elapsed / 2.0
    # round to 2 decimals
    distance = int(distance * 100 + 0.5) / 100.0
    return distance

print "starting..."
setup()
while GPIO.input(P_ESCAPE) == GPIO.LOW:
    d = getDistance()
    print "d =", d, "cm"
    time.sleep(1)
GPIO.cleanup()
print "done"
    
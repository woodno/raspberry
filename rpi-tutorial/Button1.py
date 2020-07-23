# Button1.py

import RPi.GPIO as GPIO
import time

P_BUTTON = 15 # adapt to your wiring
P_LED = 7  # adapt to your wiring

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(P_LED, GPIO.OUT)

setup()
while True:
    if GPIO.input(P_BUTTON) == GPIO.LOW:
        GPIO.output(P_LED, GPIO.HIGH)
    else:
        GPIO.output(P_LED, GPIO.LOW)
    time.sleep(0.01)

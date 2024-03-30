#Exposing random nature of pin without connections
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
testPin = 16
GPIO.setup(testPin, GPIO.IN)
while True:
    if GPIO.input(testPin):
        print('Input was HIGH')
    else:
        print('Input was LOW')
    time.sleep(0.5)

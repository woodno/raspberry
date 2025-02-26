import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, 1)
time.sleep(2)
GPIO.output(18, 0)
print ("finished")

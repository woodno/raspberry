import RPi.GPIO as GPIO
import time
#One of two numbering modes you can use and the one most used.
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
try:
    while (True):
        GPIO.output(18, True)
        print ('Im on')
        time.sleep(0.5)
        GPIO.output(18, False)
        print ('Im off')
        time.sleep(0.5)
finally:
    print ("Cleaning Up")
    GPIO.cleanup()
    print ("Done Cleaning Up")

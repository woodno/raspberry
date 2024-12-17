import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIN = 18
WAITTIME = 0.0001


GPIO.setup(PIN, GPIO.IN)
#If using internal pull up resistor include pull_up_down = GPIO.PUD_DOWN
# eg GPIO.setup(PIN, GPIO.IN , pull_up_down = GPIO.PUD_DOWN)



try:
    while (True):
        print (GPIO.input (PIN))
        time.sleep(WAITTIME)  # wait 10 ms to give CPU chance to do other things
        

finally:
    print ("Cleaning Up")
    GPIO.cleanup()
    print ("Done Cleaning Up")

import RPi.GPIO as GPIO
import time
import pickle

GPIO.setmode(GPIO.BCM)
PIN = 16
WAITTIME = 0.00000001


GPIO.setup(PIN, GPIO.OUT)
#If using internal pull up resistor include pull_up_down = GPIO.PUD_DOWN
# eg GPIO.setup(PIN, GPIO.IN , pull_up_down = GPIO.PUD_DOWN)

f=open('record.txt', 'r+b')
bitList = pickle.load(f)
f.close()

try:
    for x in bitList:
        GPIO.output(PIN, x)
        time.sleep(WAITTIME)  # wait 10 ms to give CPU chance to do other things
        

finally:
    print ("Cleaning Up")
    GPIO.cleanup()
    print ("Done Cleaning Up")

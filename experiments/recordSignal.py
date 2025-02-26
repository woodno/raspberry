import RPi.GPIO as GPIO
import time
import pickle
GPIO.setmode(GPIO.BCM)
PIN = 18
WAITTIME = 0.00000001


GPIO.setup(PIN, GPIO.IN)
#If using internal pull up resistor include pull_up_down = GPIO.PUD_DOWN
# eg GPIO.setup(PIN, GPIO.IN , pull_up_down = GPIO.PUD_DOWN)


bitList = [(GPIO.input (PIN))]
try:
    while (True):
        time.sleep(WAITTIME)  # wait 10 ms to give CPU chance to do other things
        bitList.append(GPIO.input (PIN))
       

finally:
    print ("Cleaning Up")
    f = open('record.txt', 'w+b')
    s = pickle.dump(bitList, f)
    f.close()
    GPIO.cleanup()
    print ("Done Cleaning Up")

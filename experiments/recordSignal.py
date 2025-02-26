import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
PIN = 18



GPIO.setup(PIN, GPIO.IN)
#If using internal pull up resistor include pull_up_down = GPIO.PUD_DOWN
# eg GPIO.setup(PIN, GPIO.IN , pull_up_down = GPIO.PUD_DOWN)


bitList = [(GPIO.input (PIN))]
try:
    while (True):
        bitList.append(GPIO.input (PIN))
        time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things
        

finally:
    print ("Cleaning Up")
    f = open('record.txt', 'w+b')
    s = pickle.dump(bitList, f)
    f.close()
    GPIO.cleanup()
    print ("Done Cleaning Up")
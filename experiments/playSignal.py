import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIN = 16



GPIO.setup(PIN, GPIO.OUT)
#If using internal pull up resistor include pull_up_down = GPIO.PUD_DOWN
# eg GPIO.setup(PIN, GPIO.IN , pull_up_down = GPIO.PUD_DOWN)

f=open('test.txt', 'r+b')
bitList = pickle.load(f)
f.close()

try:
    for x in bitList
        GPIO.output(PIN, x)
        time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things
        

finally:
    print ("Cleaning Up")
    GPIO.cleanup()
    print ("Done Cleaning Up")
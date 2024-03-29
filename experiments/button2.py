import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
i = 0
PIN = 18
outPin = 5
isLightOn = False

def my_callback(channel):
    print (str(channel))
    global i
    i = i + 1
    print ("Button press "+ str(i))
    global isLightOn
    isLightOn = not isLightOn
    GPIO.output(outPin, isLightOn)
        
    

GPIO.setup(PIN, GPIO.IN)
GPIO.setup(outPin, GPIO.OUT)
#If using internal pull up resistor include pull_up_down = GPIO.PUD_DOWN
# eg GPIO.setup(PIN, GPIO.IN , pull_up_down = GPIO.PUD_DOWN)
GPIO.add_event_detect(PIN, GPIO.RISING, callback = my_callback, bouncetime=100)


try:
    while (True):
        time.sleep(1)
       
finally:
    print ("Cleaning Up")
    GPIO.cleanup()
    print ("Done Cleaning Up")

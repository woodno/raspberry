import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
i = 0
PIN = 18
LEDPIN = 16


GPIO.setup(PIN, GPIO.IN)
#If using internal pull up resistor include pull_up_down = GPIO.PUD_DOWN
# eg GPIO.setup(PIN, GPIO.IN , pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(LEDPIN,GPIO.OUT)
isLedOn = False


try:
    while (True):
        while (GPIO.input(PIN) == GPIO.LOW):
            time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things
        #If we are here Pin 18 is no longer in the low position
        #which means the button has been pressed.
        i = i + 1
        print ("Button press "+ str(i))
        #First time through isLedOn is false so it is off
        #This if says if the led is off tiurn it on then change the flag to true
        if not isLedOn:
            GPIO.output(LEDPIN, True)
            isLedOn = True
        #This else says if the led is on turn it off and set the flag to false.    
        else:
            GPIO.output(LEDPIN, False)
            isLedOn = False
        #This while loop is here to make sure each press of the switch is recorded as only one press
        #Without this if you pushed the button down for more than 0.01 seconds it would record multiple
        #pushes of the switch and hence get unpredictable results.
        while (GPIO.input(PIN) == GPIO.HIGH):
            time.sleep(0.01)
       
finally:
    print ("Cleaning Up")
    GPIO.cleanup()
    print ("Done Cleaning Up")

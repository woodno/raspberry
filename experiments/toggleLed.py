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
        i = i + 1
        print ("Button press "+ str(i))
        if not isLedOn:
            GPIO.output(LEDPIN, True)
            isLedOn = True
        else:
            GPIO.output(LEDPIN, False)
            isLedOn = False
        while (GPIO.input(PIN) == GPIO.HIGH):
            time.sleep(0.01)

# try:
#     while(True):
#         if (GPIO.input(PIN) == GPIO.LOW):
#             print ("Low")
#         else:
#             print ("High")
#         time.sleep(0.01)
#         
       
finally:
    print ("Cleaning Up")
    GPIO.cleanup()
    print ("Done Cleaning Up")

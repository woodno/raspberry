import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23,1)
time.sleep(2)
print("finished")
#The purpose of pull up down is to add an internal resistor
#such that when the input is 0 the voltage is 0
#GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#def my_callback(self):
#   print ("the state of pin 17 is " + str(GPIO.input(17)))
#GPIO.add_event_detect(17, GPIO.BOTH, callback=my_callback)
#print ("The 17 input is " + str(GPIO.input(17)))
#GPIO.output(18, 1)
#print ("The 17 input is " + str(GPIO.input(17)))
#time.sleep(2)

##GPIO.output(18, 0)
##print ("The 17 input is " + str(GPIO.input(17)))
##print ("finished")

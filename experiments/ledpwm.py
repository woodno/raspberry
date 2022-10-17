import RPi.GPIO as GPIO
import time

#BCM refers to how the pins are refered to.
#See here for reference
#https://raspberrypi.stackexchange.com/
#questions/12966/
#what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
GPIO.setmode(GPIO.BCM)

led_pin = 18
GPIO.setup(led_pin, GPIO.OUT)

#This is setting the phase frequency to 500Hz
#Actually this is kind of true but the accuracy falls off
#as the frequency rises.
pwm_led = GPIO.PWM(led_pin, 500)

#This means that the led gets started at 100% of the cycle
pwm_led.start(100)
try:
    while (True):
        #change to raw_input if using python 2
        duty_s = input("Enter Brightness (0 to 100 or x to exit):")
        #TODO put in a test here to check the input is a number
        #and the number is between 0 - 100
        #if the user inputs an x exit
        duty = int (duty_s)
        pwm_led.ChangeDutyCycle(duty)
finally:
    print ("Cleaning Up")
    GPIO.cleanup()
    print ("Done Cleaning Up")

import RPi.GPIO as GPIO
import time
servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
p.start(2.5) # Initialization

def pwmOutputFromDegree (degree):
    pwm = 2.5/90 * degree + 5
    return pwm
try:
    #degree = 135
    #User validation inputs between 0 - 180 inclusive
    #User validation they input a number
    while (True):

        degree = float (input ("Enter a degree "))
        x = pwmOutputFromDegree (degree)
        print ("The pulse = " + str (x) + "% from the degree input " + str (degree))
        p.ChangeDutyCycle (x)

finally:
    print ("Cleaning Up")
    GPIO.cleanup()
    print ("Done Cleaning Up")
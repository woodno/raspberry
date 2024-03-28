#From https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/
import RPi.GPIO as GPIO
import time
servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
# From https://en.wikipedia.org/wiki/Servo_control#/media/File:Servomotor_Timing_Diagram.svg
# Now for a cycle of 50 Hz this means.....
# 
# 1.5ms = 20ms  * x/100(where x is the duty cycle) 
# 
# x = 7.5% duty cycle for 0 position
# 
# For 90 degree position
# 
# 2ms = 20ms * x/100
# 
# x = 10% duty cycle
# 
# For -90 degree position
# 
# 1ms = 20ms * x/100
# 
# x = 5%
#Creating a function to output pwm values for a servo control
#This function outputs pwm values for degrees entered for
#a servo motor
#Argument degree is the degree to turn the motor
#Expected values between 0 - 180
#Return is the pwm value to set
#Exceptions....
def pwmOutputFromDegree(degree):
    y = 2.5/90 * degree + 5
    return y

# print (pwmOutputFromDegree(45))
# print (pwmOutputFromDegree(twenty))


p.start(2.5) # Initialization
try:
  while True:
    y = float(input ("Enter a degree "))
    
    
    z = pwmOutputFromDegree(y)
    print ("Turning angle = " + str(y))
    print ("Pwm output = " +str(z))
    p.ChangeDutyCycle(z)
    
except KeyboardInterrupt:
  print("Cleaning up")
  p.stop()
  GPIO.cleanup()
  print("Clean up done")

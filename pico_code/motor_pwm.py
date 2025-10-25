from machine import Pin, PWM # we need to import PWM to use PWM
import time
# intialise pin 1 as a PWM output
pwm_pin = PWM(Pin(1))
# this sets up the frequency that the pin is turned off and on (it is not duty cycle)
# all constants should be set at the beginning of the program
# later on we will learn how to do this.
pwm_pin.freq(1000)

# Setup for the board is as follows
# vbus gets connected to the motor
# vbus only works when the microUSB is connected.
# otherwise you need to connect an external power source
# Pin 1 goes through a 220 ohm resistor to the base of the transistor
# A gnd pin needs to go to one of the ground rails
# 


# this varaible is used to help calculate the required input from a duty cycle percentage
# the value for the duty cycle is held as 2 bytes of data.
# 2^16 = 65536. 
max = 65535

def getPWMFromPercentage(percentage):
    PWM_value = int(percentage/100 * max)
    print ("My PWM_value is", PWM_value)
    return PWM_value
percentagePWM = 100
try:
    while True:
        if percentagePWM < 0:
            percentagePWM = 100
        pwm_pin.duty_u16(getPWMFromPercentage(percentagePWM))
        print ("My motor is running at ", percentagePWM , "%")
        time.sleep(2)
        percentagePWM = percentagePWM - 10
finally:
    pwm_pin.deinit()
    input_pin = Pin(1, Pin.IN)
    print ("I've cleaned up")
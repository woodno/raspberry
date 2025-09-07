from machine import Pin, PWM # we need to import PWM to use PWM
import time
# intialise pin 1 as a PWM output
pwm_enable_pin = PWM(Pin(1))
# this sets up the frequency that the pin is turned off and on (it is not duty cycle)
# all constants should be set at the beginning of the program
# later on we will learn how to do this.
pwm_enable_pin.freq(1000)


#The following pin out is in relation
#to the L293D motor driver
#this setup facilitates one motor running in forward or reverse mode
# Using more pins the driver can run another motor forward or reverse.
#This is the pin out starting from the top left (Notch is the top)
#Pin 1 enable = GPIO pin 1 (PWM pin)
#Pin 2 = GPIO pin 2
#Pin 3 OUT 1 = motor lead 1
#Pin 4 GND = GND Pi
#Pin 5 If using an external power source connect to the ground of that.
#Pin 12, 13 are also GND that can be used to ground the external power supply or Pico
#Pin 4,5,12 and 13 are internally connected so can be used for any ground. 
#Pin 6 = motor lead 2
#Pin 7 = = GPIO 3
#Pin 8 (Vs) = 3.3 V on Pico (Supplies logic power)  Can use external power.
#Pin 16 (Vss) = VBus when conected to microUSB or 5V external power otherwise.

#IC pins are numbered 1 and up anticlockwise.
# pin 16 is top right.


input1_pin = Pin(2, Pin.OUT)
input2_pin = Pin(3, Pin.OUT)





# this varaible is used to help calculate the required input from a duty cycle percentage
# the value for the duty cycle is held as 2 bytes of data.
# 2^16 = 65536. 
max = 65535

def getPWMFromPercentage(percentage):
    PWM_value = int(percentage/100 * max)
    print ("My PWM_value is", PWM_value)
    return PWM_value
percentagePWM = 100
hasForwardDirection = True
try:
    while True:
        if percentagePWM < 0:
            percentagePWM = 100
            hasForwardDirection = not hasForwardDirection
        pwm_enable_pin.duty_u16(getPWMFromPercentage(percentagePWM))
        print ("My motor is running at ", percentagePWM , "%")
        if (hasForwardDirection):
            print ("Forwards")
            input1_pin.value(1)
            input2_pin.value(0)
        else:
            print ("Backwards")
            input1_pin.value(0)
            input2_pin.value(1)
        time.sleep(2)
        percentagePWM = percentagePWM - 10
finally:
    pwm_enable_pin.deinit()
    inputpwm_pin = (1, Pin.IN)
    input1_pin = (2, Pin.IN)
    input2_pin = (3, Pin.IN)
    
    print ("I've cleaned up")
from machine import Pin, PWM # we need to import PWM to use PWM
import time
# intialise pin 1 as a PWM output
pwm_pin = PWM(Pin(1))
# this sets up the frequency that the pin is turned off and on (it is not duty cycle)
# servo motors generally work on 50Hz
pwm_pin.freq(50)

# this varaible is used to help calculate the required input from a duty cycle percentage
# the value for the duty cycle is held as 2 bytes of data.
# 2^16 = 65536. 
max = 65535

#Pin set up
#GPIO 1 = Yellow
#GND = Brown
#3.3V = Red

#Gets a micropython expected duty cycle from a percentage
def getPWMFromPercentage(percentage):
    PWM_value = int(percentage/100 * max)
    print ("My PWM_value is", PWM_value)
    return PWM_value
#expected inputs are -90 to 90
def pwmPercFromDegree (degree):
    if degree < -90 or degree > 90:
       raise Exception ("Input out of range")
    pwm = 2.5/90 * degree + 7.5 #2.5/90 = 0.0278 approx
    return pwm

try:
    while True:
        deg_req_str = input ("Enter a degree between -90 to 90")
        deg_req = float (deg_req_str)
        per_duty_cycle = pwmPercFromDegree(deg_req)
        u16_duty_cycle = getPWMFromPercentage(per_duty_cycle)
        print ("You want a rotor angle of ", deg_req_str)
        print ("That translates to a duty cycle of ", per_duty_cycle, "%")
        pwm_pin.duty_u16(u16_duty_cycle)
               


finally:
    pwm_pin.deinit()
    inputpwm_pin = (1, Pin.IN)  
    print ("I've cleaned up")
from machine import Pin, PWM # we need to import PWM to use PWM
import time
# intialise pin 1 as a PWM output
pwm_pin = PWM(Pin(1))

# this sets up the frequency that the pin is turned off and on (it is not duty cycle)
# all constants should be set at the beginning of the program
# later on we will learn how to do this.
pwm_pin.freq(1000)

# this varaible is used to help calculate the required input from a duty cycle percentage
# the value for the duty cycle is held as 2 bytes of data.
# 2^16 = 65536. 
MAX_PWM = 65535

try:
    while True:
        # here we multiply MAX_PWM by the desired duty cycle (as a decimal), 0.2 is 20%, 0.7 is 70% and so on
        # later on we will do calculations like this in a function
        PWM_value = int(0.2 * MAX_PWM)
        # this line is the command that actually sets the duty cycle
        pwm_pin.duty_u16(PWM_value)
        print("My LED is 20% bright")
        time.sleep (2)
        PWM_value = int(0.5 * MAX_PWM)
        pwm_pin.duty_u16(PWM_value)
        print("My LED is 50% bright")
        time.sleep (2)
        PWM_value = int(0.75 * MAX_PWM)
        pwm_pin.duty_u16(PWM_value)
        print("My LED is 75% bright")
        time.sleep (2)
        PWM_value = int(1 * MAX_PWM)
        pwm_pin.duty_u16(PWM_value)
        print("My LED is 100% bright")
        time.sleep (2)
finally:
    
    pwm_pin.deinit()
    print ("pwm_pin.duty_u16() = ",pwm_pin.duty_u16())
    input_pin = Pin(1, Pin.IN)
    print("input_pin.value() = ",input_pin.value())  
    print ("I've cleaned up")
    
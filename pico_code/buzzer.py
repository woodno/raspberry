from machine import Pin, PWM # we need to import PWM to use PWM
import time
# intialise pin 1 as a PWM output
pwm_pin = PWM(Pin(1))
# this sets up the frequency that the pin is turned off and on (it is not duty cycle)
# all constants should be set at the beginning of the program
# later on we will learn how to do this.
init_freq = 1000
pwm_pin.freq(init_freq)

# this varaible is used to help calculate the required input from a duty cycle percentage
# the value for the duty cycle is held as 2 bytes of data.
# 2^16 = 65536. 
max = 65535
freq = init_freq
try:
    while freq < 20000:
        # Hear we are basically making the buzzer move back and forth.
        PWM_value = int(0.5 * max)
        pwm_pin.duty_u16(PWM_value)
        print("My buzzer is at ", freq, " Hertz")
        time.sleep (1)
        freq = freq + 1000
        pwm_pin.freq(freq)
finally:
    pwm_pin.deinit()
    input_pin = (1, Pin.IN)
    print ("I've cleaned up")
    
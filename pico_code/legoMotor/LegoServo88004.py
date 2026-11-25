#https://scuttlebots.com/2014/03/02/lego-pf-hacking-wiring

#Lego Servo 88004
#Not correct code needs some fixing
from machine import Pin, PWM
import time

# Configure Pins for L298N or similar motor driver
# C1 and C2 are the control lines for the 88004
pwm_enable_pin = PWM(Pin(10))
pwm_enable_pin.freq(1150)
max = 65535

c1 = Pin(6, Pin.OUT)
c2 = Pin(7, Pin.OUT)
# Set Frequency to 1150 Hz as required by LEGO 88004
#Some people suggest 1200
def getPWMFromPercentage(percentage):
    PWM_value = int(percentage/100 * max)
    print ("My PWM_value is", PWM_value)
    return PWM_value
percentagePWM = 100
hasADirection = True


# --- Main Program ---

try:
    while True:
        if percentagePWM < 0:
            percentagePWM = 100
            hasADirection = not hasADirection
        pwm_enable_pin.duty_u16(getPWMFromPercentage(percentagePWM))
        print ("My motor is running at ", percentagePWM , "%")
        if (hasADirection):
            print ("A Direction")
            c1.value(1)
            c2.value(0)
        else:
            print ("B Direction")
            c1.value(0)
            c2.value(1)
        time.sleep(2)
        percentagePWM = percentagePWM - 10
finally:
    pwm_enable_pin.deinit()
    inputpwm_pin = Pin(10, Pin.IN)
    input1_pin = Pin(6, Pin.IN)
    input2_pin = Pin(7, Pin.IN)
    # LEGO "Servo Motor" has little to do with a RC servomotor. To drive it, you need to:
# 
# Power it at 9V (probably works at 5 volts, but with less torque) through PWR/GND terminals
# To move in one direction, send a PWM signal (1200 Hz, 0 to 100% duty cycle) on C1 and keep C2 at GND level. As duty cycle varies, servo motor will move along 7 positions on one side. See this video.
# To move in the other direction and reach the 7 other positions, send PWM to C2 and keep C1 at ground level.
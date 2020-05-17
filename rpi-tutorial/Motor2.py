# Motor2.py
# Motor speed & direction 

import RPi.GPIO as GPIO
import time

P_MOTA1 = 18
P_MOTA2 = 22
fPWM = 50  # Hz (not higher with software PWM)

def forward(speed):
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(0)

def backward(speed):        
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(speed)
    
def stop():
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)

def setup():
    global pwm1, pwm2
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_MOTA1, GPIO.OUT)
    pwm1 = GPIO.PWM(P_MOTA1, fPWM)
    pwm1.start(0)
    GPIO.setup(P_MOTA2, GPIO.OUT)
    pwm2 = GPIO.PWM(P_MOTA2, fPWM)
    pwm2.start(0)
    
print "starting"
setup()
for speed in range(10, 101, 10):
    print "forward with speed", speed
    forward(speed)
    time.sleep(2)
for speed in range(10, 101, 10):
    print "backward with speed", speed
    backward(speed)
    time.sleep(2)
print "stopping"
stop()
GPIO.cleanup()    
print "done"

#h_bridge.py Part L2930
import RPi.GPIO as GPIO
import time
enable_pin = 18
in1_pin = 23
in2_pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)
GPIO.setup(enable_pin, GPIO.OUT)
pwm = GPIO.PWM (enable_pin, 500)
pwm.start(0)
def clockwise():
    #GPIO.output(enable_pin, False)
    GPIO.output(in1_pin, True)
    GPIO.output(in2_pin,False)
def counter_clockwise():
    #GPIO.output(enable_pin, False)
    GPIO.output(in1_pin, False)
    GPIO.output(in2_pin,True)

try:

    
    while (True):
        #change to raw_input if using python 2
        cmd = input("Command, f/r 0..9, Eg f5 :")
        print (cmd[0])
        print (cmd[1])
        direction =cmd[0]
        #pwm.stop()
        #time.sleep(1)
        if direction == "f":
            clockwise()
        else:
            counter_clockwise()
        speed = int(cmd[1]) * 10
        pwm.ChangeDutyCycle(speed)

finally:
    print ("Cleaning Up")
    GPIO.cleanup()
    print ("Done Cleaning Up")

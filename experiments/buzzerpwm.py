import RPi.GPIO as GPIO
import time
#PWM code at https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
buzzer_pin = 18
GPIO.setmode (GPIO.BCM)
GPIO.setup (buzzer_pin, GPIO.OUT)

def buzz (pitch, duration):
    pwm_buzz = GPIO.PWM(buzzer_pin, pitch)
    #50 means it is on 50% of the time.
    pwm_buzz.start(50)
    print ("Pitch is " + str(pitch) + "Hz")
    print ("Duration is " + str(duration) + "seconds")
    time.sleep(duration)
    pwm_buzz.stop()
    
try:
    while True:
        #Change to raw_input for python
        pitch_s = input ("Enter Pitch 200 to 2000 ")
        #Trace pitch = 1000
        pitch = float (pitch_s)
        duration_s = input ("Enter duration seconds ")
        #Trace duration  = 4
        duration = float (duration_s)
        buzz (pitch, duration)
        
finally:
    print ("Cleaning Up")
    GPIO.cleanup()
    print ("Done Cleaning Up")


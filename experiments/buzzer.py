import RPi.GPIO as GPIO
import time
buzzer_pin = 18
GPIO.setmode (GPIO.BCM)
GPIO.setup (buzzer_pin, GPIO.OUT)
def buzz (pitch, duration):
    print ("Pitch is " + str(pitch) + "Hz")
    print ("Duration is " + str(duration) + "seconds")
    period = 1.0 / pitch
    print ("Period is " + str(period) + "seconds")
    delay = period / 2
    cycles = int (duration * pitch)
    print ("Cycles are " + str(cycles))
    #range function returns a sequence of numbers
    for i in range (cycles):
        #print ("Range (cycles) returns " + range (cycles))
        GPIO.output (buzzer_pin, True)
        time.sleep(delay)
        GPIO.output (buzzer_pin, False)
        time.sleep(delay)
try:
    while True:
        #Change to raw_input for python
        pitch_s = input ("Enter Pitch 200 to 2000 ")
        pitch = float (pitch_s)
        duration_s = input ("Enter duration seconds ")
        duration = float (duration_s)
        buzz (pitch, duration)
        
finally:
    print ("Cleaning Up")
    GPIO.cleanup()
    print ("Done Cleaning Up")

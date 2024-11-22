#From https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/
import RPi.GPIO as GPIO
import time
servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
# From https://en.wikipedia.org/wiki/Servo_control#/media/File:Servomotor_Timing_Diagram.svg
# Now for a cycle of 50 Hz this means.....
# Servo motors work for values between 5% and 10% of the pulse.
# (Usually consult datasheet.) 
# Angle = 0 for 5%
# Angle = 90 for 7.5%
# Angle = 180 for 10%

p.start(2.5) # Initialization
try:
  while True:
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
except KeyboardInterrupt:
  print("Cleaning up")
  p.stop()
  GPIO.cleanup()
  print("Clean up done")

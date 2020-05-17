import RPi.GPIO as GPIO
import time

P_LED = 7  # adapt to your wiring

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_LED, GPIO.OUT)

print "starting"
setup()
i = 0
while i < 5:
    print i
    GPIO.output(P_LED, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(P_LED, GPIO.LOW)
    time.sleep(0.1)
    i += 1
GPIO.cleanup()
print "done"

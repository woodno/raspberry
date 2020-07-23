# Sound2b.py

import RPi.GPIO as GPIO
from soundplayer import SoundPlayer
import time

P_LED = 18 # adapt to your wiring

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_LED, GPIO.OUT)
    
setup()
# Sine of 1000 Hz during 5 s, non-blocking, device 0
SoundPlayer.playTone(1000, 5, False, 0)
while SoundPlayer.isPlaying():
    GPIO.output(P_LED, GPIO.HIGH)
    print "on"
    time.sleep(0.5)
    GPIO.output(P_LED, GPIO.LOW)
    print "off"
    time.sleep(0.5)

print "done"
    

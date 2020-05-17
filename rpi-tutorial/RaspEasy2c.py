# RaspEasy2c.py
# Button counter, use Oled or PyTell display

import RPi.GPIO as GPIO
import time
from OLED1306 import OLED1306
#from pytell import PyTell

P_BUTTON = 12 # Button A

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN)

print "starting..."
oled = OLED1306()
oled.setFontSize(50)
#pyTell = PyTell()

setup()
count = 0
oled.setText(str(count))
#  pyTell.showText("%4d" %count)
isButtonPressed = False
while True:
    if GPIO.input(P_BUTTON) == GPIO.HIGH and not isButtonPressed:
        isButtonPressed = True
        count += 1
        oled.setText(str(count))
#        pyTell.showText("%4d" %count)
        time.sleep(0.1)
    elif GPIO.input(P_BUTTON) == GPIO.LOW and isButtonPressed:
        isButtonPressed = False
        time.sleep(0.1)
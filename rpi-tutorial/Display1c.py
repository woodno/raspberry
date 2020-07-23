# Display1c.py

from pytell import PyTell
import time

pt = PyTell()
pt.showText("run")
time.sleep(3)

text = "HELLO Python"
pt.showTicker(text, count = 2, speed = 4, blocking = True)

text = "8ye"
pt.showBlinker(text, dp = [0, 0, 0, 1], count = 4, speed = 2, blocking = True)

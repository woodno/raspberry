# Display3c.py

from py7seg import Py7Seg
import time

ps = Py7Seg()
ps.setBrightness(7)
ps.showText("run")
time.sleep(3)

text = "HELLO Python"
ps.showTicker(text, count = 2, speed = 4, blocking = True)

text = "8ye"
ps.showBlinker(text, dp = [0, 0, 0, 1], count = 4, speed = 2, blocking = True)
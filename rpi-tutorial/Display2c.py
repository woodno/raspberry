# Display2c.py

from Disp4tronix import Disp4tronix
import time

dp = Disp4tronix()
dp.showText("run")
time.sleep(3)

text = "HELLO Python"
dp.showTicker(text, count = 2, speed = 4, blocking = True)

text = "8ye"
dp.showBlinker(text, dp = [0, 0, 0, 1], count = 4, speed = 2, blocking = True)

# Display106a.py
# Ticker, constructor with parameters

from pytell import PyTell

pt = PyTell()
ip = "x192-168-1-13"
pt.showTicker(ip, count = 2, speed = 4, blocking = True)
pt.showText("donE")

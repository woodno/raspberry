# Sound1c.py

import time
from soundplayer import SoundPlayer

# Use device with ID 1  (mostly USB audio adapter)
#p = SoundPlayer("/home/pi/Music/jew1.mp3", 1)        
p = SoundPlayer("/home/pi/Music/jew1.wav", 1)        
print "play whole song"
p.play(1, True) # non-blocking, volume = 1
print "done"


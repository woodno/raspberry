# Sound1b.py

from soundplayer import SoundPlayer
import RPi.GPIO as GPIO
import time

'''
states:
STOPPED : play process terminated
PAUSED: play process stopped (playing still underway)
PLAYING: play process executing
'''

# Button pins, adapt to your configuration
P_PLAY = 24 
P_PAUSE = 16
P_STOP = 22
P_SELECT = 12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_STOP, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(P_PAUSE, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(P_PLAY, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(P_SELECT, GPIO.IN, GPIO.PUD_UP)
 
setup()
nbSongs = 4
songID = 0
p = SoundPlayer("/home/pi/songs/song" + str(songID) + ".mp3", 1)        
p.play()
print "playing, song ID", songID
state = "PLAYING"

while True:
    if GPIO.input(P_PAUSE) == GPIO.LOW and state == "PLAYING":
        state = "PAUSED"
        print "playing->paused"
        p.pause()
    elif GPIO.input(P_PLAY) == GPIO.LOW and state == "STOPPED":
        state = "PLAYING"
        print "stopped->playing, song ID", songID
        p.play()
    elif GPIO.input(P_PLAY) == GPIO.LOW and state == "PAUSED":
        state = "PLAYING"
        print "paused->playing"
        p.resume()
    elif GPIO.input(P_STOP) == GPIO.LOW and (state == "PAUSED" or state == "PLAYING"):
        state = "STOPPED"
        print "paused/playing->stopped"
        p.stop()
    elif (GPIO.input(P_SELECT) == GPIO.LOW and state == "STOPPED") \
          or (state == "PLAYING" and not p.isPlaying()):
        songID += 1
        if songID == nbSongs:
            songID = 0
        p = SoundPlayer("/home/pi/songs/song" + str(songID) + ".mp3", 1)
        print "stopped->playing, song ID", songID
        p.play()
        state = "PLAYING"
    time.sleep(0.1) # Do not waste processor time    

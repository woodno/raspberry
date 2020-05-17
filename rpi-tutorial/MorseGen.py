# MorseGen.py

import RPi.GPIO as GPIO
import time

P_BUZZER = 22 # adapt to your wiring
dt = 0.1 # adapt to your Morse speed

morse = {
'a':'.-'   , 'b':'-...' , 'c':'-.-.' , 'd':'-..'  , 'e':'.'    ,
'f':'..-.' , 'g':'--.'  , 'h':'....' , 'i':'..'   , 'j':'.---' ,
'k':'-.-'  , 'l':'.-..' , 'm':'--'   , 'n':'-.'   , 'o':'---'  ,
'p':'.--.' , 'q':'--.-' , 'r':'.-.'  , 's':'...'  , 't':'-'    ,
'u':'..-'  , 'v':'...-' , 'w':'.--'  , 'x':'-..-' , 'y':'-.--' ,
'z':'--..' , '1':'.----', '2':'..---', '3':'...--', '4':'....-',
'5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
'0':'-----', '-':'-....-', '?':'..--..', ',':'--..--', ':':'---...',
'=':'-...-'}

def s(n):  # wait
    time.sleep(n * dt)

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUZZER, GPIO.OUT)
    
def dot():
    GPIO.output(P_BUZZER, GPIO.HIGH)
    s(1)
    GPIO.output(P_BUZZER, GPIO.LOW)
    s(1)

def dash():
    GPIO.output(P_BUZZER, GPIO.HIGH)
    s(3)
    GPIO.output(P_BUZZER, GPIO.LOW)
    s(1)

def transmit(text):
    for c in text:
        if c == " ":
            s(4)
        else:
            c = c.lower()
            if c in morse:
                k = morse[c]
                for x in k:
                    if x == '.':
                        dot()
                    else:
                        dash()
            s(2)

setup()
transmit("cq de hb9abh pse k")
GPIO.cleanup()
print "all done"

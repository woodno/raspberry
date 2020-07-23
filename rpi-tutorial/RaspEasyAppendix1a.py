# RaspEasyAppendix1a.py
# Start/Stop, Morse calling worker thread

import RPi.GPIO as GPIO
import time
from threading import Thread

RUN_BUTTON = 12 # Button A
EXIT_BUTTON = 13 # Button B
P_BUZZER = 40 # adapt to your wiring
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

text = "cq de hb9abh pse k"

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
    sent = ""
    for c in text:
        if not transmitting:
            break 
        sent += c
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

class WorkerThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.isAlive = True
        self.isHold = True
        self.start()
        
    def run(self):
        global isPaused
        while self.isAlive:
            if self.isHold:
                time.sleep(0.1)
            else: 
                transmit(text)
                self.isHold = True
                isPaused = True

    def kill(self):
        global transmitting
        transmitting = False
        self.isAlive = False

    def hold(self):
        global transmitting
        transmitting = False
        self.isHold = True

    def resume(self):
        global transmitting
        transmitting = True
        self.isHold = False
                                        
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RUN_BUTTON, GPIO.IN)
    GPIO.setup(EXIT_BUTTON, GPIO.IN)
    GPIO.setup(P_BUZZER, GPIO.OUT)
    GPIO.output(P_BUZZER, GPIO.LOW) # Turn off buzzer

setup()
isPaused = True
isRunButtonPressed = False
isExiting = False
worker = WorkerThread()
while not isExiting:
    if GPIO.input(RUN_BUTTON) == GPIO.HIGH and not isRunButtonPressed:
        isRunButtonPressed = True
        if isPaused:    
            isPaused = False
            worker.resume()
        else:
            isPaused = True
            worker.hold()
    elif GPIO.input(RUN_BUTTON) == GPIO.LOW and isRunButtonPressed:
        isRunButtonPressed = False

    if GPIO.input(EXIT_BUTTON) == GPIO.HIGH:
        isExiting = True

    time.sleep(0.1)

worker.kill()        
GPIO.cleanup() 
print "Programm terminated"
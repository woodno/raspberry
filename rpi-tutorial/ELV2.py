# ELV2.py
# Demo program for the 7-segment display/4 button panel from ELV (www.elv.de)

from button import *
from py7seg import Py7Seg

P_BUTTON1 = 15 # adapt to your wiring
P_BUTTON2 = 19 #adapt to your wiring
P_BUTTON3 = 21 # adapt to your wiring
P_BUTTON4 = 23 # adapt to your wiring

def setup():
    global button1, button2, button3, button4
    GPIO.setmode(GPIO.BOARD)
    button1 = Button(P_BUTTON1)
    button2 = Button(P_BUTTON2)
    button3 = Button(P_BUTTON3)
    button4 = Button(P_BUTTON4)
    button1.addXButtonListener(onButtonEvent)
    button2.addXButtonListener(onButtonEvent)
    button3.addXButtonListener(onButtonEvent)
    button4.addXButtonListener(onButtonEvent)

def onButtonEvent(button, event):
    global isCounting, isUp, isReset, isAbout, count
    if button == button1:
        if event == BUTTON_CLICKED:
            if isCounting:
                isCounting = False
            else:
                isCounting = True
        elif event == BUTTON_DOUBLECLICKED:
            isAbout = True
            isCounting = False
    elif button == button2 and event == BUTTON_PRESSED:
        isUp = True
    elif button == button3 and event == BUTTON_PRESSED:
        isUp = False
    elif button == button4 and event == BUTTON_PRESSED:
        isReset = True
              
setup()
ps = Py7Seg()
ps.showText("init")
time.sleep(2)
ps.showText("stop")
isCounting = False
isReset = False
count = 0
isUp = True
isAbout = False
while True:
    if isCounting:
        text = "%4d" %count # right adjusted
        ps.showText(text)
        time.sleep(0.01)
        if isUp:
           count += 1
        else:
           count -= 1
        if count == 9999:   
            count = 0
        elif count == 0:   
            count = 9999
    else:
         ps.showText("stop")        
    if isReset:
        isReset = False
        ps.showBlinker("rset", count = 3, speed = 2, blocking = True)
        count = 0
        isUp = True
    if isAbout: 
        isAbout = False   
        ps.showTicker("diSPLAY test", count = 1, speed = 1, blocking = True)
    time.sleep(0.01)       

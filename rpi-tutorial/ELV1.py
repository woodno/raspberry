# ELV1.py
# Demo program for the 7-segment display/4 button panel from ELV (www.elv.de)

from button import *

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
    global isRunning
    if button == button1:
        print "event from button1",
    elif button == button2:
        print "event from button2",
    elif button == button3:
        print "event from button3",
    elif button== button4:
        print "event from button4",
    if event == BUTTON_PRESSED:
        print "pressed"
    elif event == BUTTON_RELEASED:
        print "released"
    elif event == BUTTON_LONGPRESSED:
       print "long pressed"
    elif event == BUTTON_CLICKED:
        print "clicked"
    elif event == BUTTON_DOUBLECLICKED:
        print "double clicked"
        if button == button1:
            isRunning = False
       
setup()
isRunning = True
count = 0
while isRunning:
    print count
    count += 1
    time.sleep(1)
GPIO.cleanup()
print "all done"
from machine import Pin # Import pin from the machine library
import time # Import time library which lets us use the sleep command

#p2 = Pin(2, Pin.IN, Pin.PULL_UP)
#p2 = Pin(2, Pin.IN, Pin.PULL_DOWN)
p2 = Pin(2, Pin.IN)
i = 0
while (True):
    while (p2.value() == 0):
        time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things
    i = i + 1
    print ("Button press "+ str(i))
    while (p2.value() == 1):
        time.sleep(0.01)

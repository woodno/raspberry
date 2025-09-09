from machine import Pin # Import pin from the machine library
import time # Import time library which lets us use the sleep command

#p2 = Pin(2, Pin.IN, Pin.PULL_UP)
#p2 = Pin(2, Pin.IN, Pin.PULL_DOWN)
p2 = Pin(2, Pin.IN)

while (True):
        print (p2.value())
        time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things
    
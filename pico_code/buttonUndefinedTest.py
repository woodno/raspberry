#This shows an undefined input pin.
#p2's value should fluctuate as it does not have a pull up or pull down resistor
from machine import Pin # Import pin from the machine library
import time # Import time library which lets us use the sleep command

#Uncomment the pull up pr pull down line and 
#comment out the line without the pull up or pull down mentioned
#p2 = Pin(2, Pin.IN, Pin.PULL_UP)
#p2 = Pin(2, Pin.IN, Pin.PULL_DOWN)
p2 = Pin(2, Pin.IN)

while (True):
        print (p2.value())
        time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things
    
from machine import Pin # Import pin from the machine library
import time # Import time library which lets us use the sleep command
led = Pin("LED", Pin.OUT) # Set up the onboard LED (can replace "LED" with a pin GPIO number)
toggleBlinker = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

i=0
#makes the led blink
isLedBlinkingOn = True
#is one unit of blinking
isLedOn = True

isTriggerReset = True
try:
    while true:
        if toggleBlinker.value() == 1:
            isTriggerReset = True
        #isTriggerReset pevents one
        #push of the switch being
        #recorded as multipe toggles.
        if toggleBlinker.value() == 0 and isTriggerReset:
            isLedBlinkingOn = not isLedBlinkingOn
            isTriggerReset = False
            if isLedBlinkingOn:
                #Not really needed
                #Led would blink on second run
                isLedOn = true
            else:
                #makes sure led is left in an off state
                led.value(0)
        
        if isLedBlinkingOn:
            led.value(isLedOn)  # Turn the LED ON
            isLedOn = not isLedOn
            print ("im here after run " + str(i) )
            i = i + 1
            
        time.sleep(0.5) # Go to sleep for 0.5 seconds

finally:
	led.value(0)
	led = Pin("LED", Pin.IN) 
	print ("I've cleaned up after " + str(i) + " runs")
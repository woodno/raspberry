from machine import Pin # Import pin from the machine library
import time # Import time library which lets us use the sleep command

led = Pin(1, Pin.OUT) # Set up the onboard LED (can replace "LED" with a pin GPIO number)
i=0
try:
    while True:  # Loop forever
        led.value(1)  # Turn the LED ON
        time.sleep(2) # Go to sleep for 2 seconds
            
        led.value(0)  # Turn the LED OFF
        time.sleep(2) # Go to sleep for 2 seconds
        i= i + 1
        print ("im here after run " + str(i) )

finally:
	led.value(0)
	led = Pin(1, Pin.IN) 
	print ("I've cleaned up after " + str(i) + " runs")


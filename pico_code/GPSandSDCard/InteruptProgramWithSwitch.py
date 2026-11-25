#Used to interupt a progam
#In our case as template for GPS recording
from machine import Pin
import time

# Global variable to track state or flag
switch_triggered = False

# ISR handler function
def handle_switch(pin):
    global switch_triggered
    switch_triggered = True

# Configure the switch on GPIO 14 with a pull-up resistor
switch_pin = Pin(14, Pin.IN, Pin.PULL_UP)

# Attach the interrupt to the falling edge (when switch connects to ground)
switch_pin.irq(trigger=Pin.IRQ_FALLING, handler=handle_switch)

print("Running main program... Throw the switch.")

while True:
    if switch_triggered:
        print("Switch was thrown! Interrupt handled.")
        switch_triggered = False  # Reset the flag
    
    # Your regular main loop code goes here
    time.sleep(0.1)

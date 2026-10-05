#Adapt this code to stop main.py with a switch.

import machine
import sys

# Use a physical wire to connect GP15 to GND to stop the script
safety_pin = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
if safety_pin.value() == 0: 
    print("Safety switch activated. Exiting script.")
    sys.exit() # Safely stops execution before the main loop begins
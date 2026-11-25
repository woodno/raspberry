#TODO Adapt this code to toggle main.py blinking with a switch.

import machine
import sys
import time

# Use a physical wire to connect GP15 to GND to stop the script

stop_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
while True:
    if stop_pin.value() == 0: 
        print("Safety switch activated. Exiting script.")
        sys.exit() # Safely stops execution before the main loop begins
    print ("Before sleep")
    time.sleep(0.1)

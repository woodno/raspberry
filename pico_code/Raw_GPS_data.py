#Raw GPS Data
#From https://core-electronics.com.au/guides/raspberry-pi-pico/how-to-add-gps-to-a-raspberry-pi-pico/#using-a-gps-library
from machine import Pin, UART
import time

# Set up UART connection to GPS module
#The tx pin on the pico (pin 0) gets connected to the
#rx pin on the GPS module
#The rx pin on the pico (pin 1 )
#gets connected to the tx pin on the gps module
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Main loop
while True:
    # Check if data is available from GPS
    if uart.any():
        # Read the available data
        gps_reading = uart.read().decode('utf-8')
        
        print(gps_reading)
#Using GPS Library
#From #From https://core-electronics.com.au/guides/raspberry-pi-pico/how-to-add-gps-to-a-raspberry-pi-pico/#using-a-gps-library
from machine import Pin, UART
import time
import gps_parser  # Import our GPS parser library
# Set up UART connection to GPS module
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Create a GPS reader object
gps = gps_parser.GPSReader(uart)

# Main loop
while True:
    # Get the GPS data, this will also try and read any new information form the GPS
    gps_data = gps.get_data()
    
    # Print the GPS data
    print(gps_data.has_fix, gps_data.latitude, gps_data.longitude)
    
    # Small delay
    time.sleep(0.5)
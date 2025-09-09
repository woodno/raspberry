from machine import Pin, ADC # we need to import ADC to use analog inputs
import time
#26, 27,28 are the only ADC pins
# set up pin 26 as an analog input
pot = ADC(Pin(26)) 
max_u16 = 65535
max_vol_input = 3.3
# constant to convert the 0 - 65535 range to 0 - 3.3 volts
conversion_factor = max_vol_input / max_u16

while True:
    # read analog input and store it in a variable called pot_voltage
    pot_voltage = pot.read_u16()
  
    # print pot_voltage
    print(pot_voltage)
    time.sleep(0.1) 
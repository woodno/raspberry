# Display3a.py

import smbus
import time

i2c_address = 0x38
bus = smbus.SMBus(1)  # RPi revision 2 (0 for revision 1)

def setup():
    instruction_byte = 0x00
    control_byte = 0b00010111 
    # b0 = 1: dynamic mode (autoincrement digits)  
    # b1 = 1: digit 1/3 not blanked, b2 = 1: digit 2/4 not blanked
    # b4 = 1: 3 mA segment current 
    # write to control register
    bus.write_byte_data(i2c_address, instruction_byte, control_byte)

def clear():
    bus.write_i2c_block_data(i2c_address, 1, [0, 0, 0, 0])
   
setup()
data = [63, 6, 91, 79] # 0123
# write starting from digit 1
bus.write_i2c_block_data(i2c_address, 1, data)
time.sleep(5)
clear()

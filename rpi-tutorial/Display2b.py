# Display2b.py

from smbus import SMBus
import time

def setup():
    bus.write_byte_data(i2c_address, 0x00, 0x00) # Set all of bank 0 to outputs
    bus.write_byte_data(i2c_address, 0x01, 0x00) # Set all of bank 1 to outputs

def setValue(val, digit):
    '''
    @param digit: 0: leftmost digit
    @param val: 0..255: segment value
    '''
    n = (1 << (3 - digit)) ^ 255
    bus.write_byte_data(i2c_address, 0x13, n)
    bus.write_byte_data(i2c_address, 0x12, val)

i2c_address = 0x20
bus = SMBus(1) # For revision 2 Raspberry Pi
setup()
word = [118, 119, 56, 63]  # HALO
while True:
    for i in range(4):
        setValue(word[i], i)
        time.sleep(0.002)
        setValue(0, i)
        time.sleep(0.002)




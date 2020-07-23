# Display1a.py
# Write 4 bytes (integers)

import smbus

i2c_address = 0x20
bus = smbus.SMBus(1)  # RPi revision 2 (0 for revision 1)
cmd = 1 # segment mode
data = [63, 6, 91, 79] # 0123
bus.write_block_data(i2c_address, cmd, data)

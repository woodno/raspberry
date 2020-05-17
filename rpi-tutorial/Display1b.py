# Display1b.py

import smbus
import time

PATTERN = {' ': 0, '!': 134, '"': 34, '#': 0, '$': 0, '%': 0, '&': 0, '\'': 2, '(': 0, ')': 0,
           '*': 0, '+': 0, ',': 4, '-': 64, '.': 128, '/': 82, '0': 63, '1': 6, '2': 91, '3': 79,
           '4': 102, '5': 109, '6': 125, '7': 7, '8': 127, '9': 111, ':': 0, ';': 0, '<': 0,
           '=': 72, '>': 0, '?': 0, '@': 93, 'A': 119, 'B': 124, 'C': 57, 'D': 94, 'E': 121,
           'F': 113, 'G': 61, 'H': 118, 'I': 48, 'J': 14, 'K': 112, 'L': 56, 'M': 85, 'N': 84,
           'O': 63, 'P': 115, 'Q': 103, 'R': 80, 'S': 45, 'T': 120, 'U': 62, 'V': 54, 'W': 106,
           'X': 73, 'Y': 110, 'Z': 27, '[': 57, '\\': 100, ']': 15, '^': 35, '_': 8, '`': 32,
           'a': 119, 'b': 124, 'c': 88, 'd': 94, 'e': 121, 'f': 113, 'g': 61, 'h': 116, 'i': 16,
           'j': 12, 'k': 112, 'l': 48, 'm': 85, 'n': 84, 'o': 92, 'p': 115, 'q': 103, 'r': 80, 's': 45,
           't': 120, 'u': 28, 'v': 54, 'w': 106, 'x': 73, 'y': 110, 'z': 27, '{': 0, '|': 48, '}': 0, '~': 65}


def toSegment(text):
   data = []
   for c in text:
       data.append(PATTERN[c])
   return data

i2c_address = 0x20
bus = smbus.SMBus(1)  # RPi revision 2 (0 for revision 1)
cmd = 1 # segment mode
text = "run "
data = toSegment(text)
bus.write_block_data(i2c_address, cmd, data)
time.sleep(3)
for i in range(1001):
    text = "%4d" %i # right adjusted
    data = toSegment(text)
    bus.write_block_data(i2c_address, cmd, data)
    time.sleep(0.01)
time.sleep(3)
text = "donE"
data = toSegment(text)
bus.write_block_data(i2c_address, cmd, data)

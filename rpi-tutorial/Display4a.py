# Display4a.py

import RPi.GPIO as GPIO

from OLED1306 import OLED1306

print "Writing to display"
disp = OLED1306()
disp.setText("Hello Python")
print "done"

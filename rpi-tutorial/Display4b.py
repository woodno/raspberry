# Display4b.py

from OLED1306 import OLED1306

disp = OLED1306("/home/pi/Pictures/einstein.ppm")
disp.setText("God\ndoes not\nplay dice!", 0, 15, 60) 
# Parameters: text, line number, font size, indent (pixels)

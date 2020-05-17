# Display4c.py

from OLED1306 import OLED1306
import time

disp = OLED1306()
nb = 1
while True:
    disp.println("Line #" + str(nb))
    nb += 1
    time.sleep(0.5)

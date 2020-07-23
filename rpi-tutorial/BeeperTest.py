# Infrared2.py
# GP2Y0A21YK sensor with PCF8591 ADC

from Beeper import Beeper

P_BUZZER = 22
beeper = Beeper(P_BUZZER)
beeper.start(0.05, 0, 100, True) # to say we are ready
print "All done"

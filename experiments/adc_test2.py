from gpiozero import MCP3008
#requires gpiozero installed
#sudo apt update
#sudo apt install python3-gpiozero
#doco at https://gpiozero.readthedocs.io/en/stable/api_spi.html
#Clockwise from top right
#Pin 16 VDD - 3.3 V
#Pin 15 VREF -3.3 V
#Pin 14 AGND -GND
#Pin 13 CLK - SCLK
#Pin 12 DOUT - MISO
#Pin 11 DIn -MOSI
#Pin 10 CS/SHDN -CE0
#Pin 9 DGND - GND
#Pin 1 Ch 0 (Top left pin) - Analog input being measured.
#For the test a 3.3 V input was output to an outside pin of a pot
#The middle pin of the pot was connected to the Channel 0 input
#The other outside pin was put to a ground.
#A voltage divider should be used to ensure the voltage is not exceeded.

import time
analog_input = MCP3008(channel=0,clock_pin=11,mosi_pin=10,
                       miso_pin=9,select_pin=8)
MAXANALOGINPUT = 5
while True:
    #value is between 0 - 1
    reading = analog_input.value
    voltage = reading * MAXANALOGINPUT
    print("Reading = {:.2f}\tVoltage = {:.2f}".format(reading,voltage))
    time.sleep(1)
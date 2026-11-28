#Listen for any messages and report them
from PiicoDev_Transceiver import PiicoDev_Transceiver
from PiicoDev_Unified import sleep_ms

radio = PiicoDev_Transceiver()

while True:
    if radio.receive():
        message = radio.message
        print(message)
    sleep_ms(50)
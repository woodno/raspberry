#This will save some text to the sd card as
#a hello wold test that the card works
#I've added some tasks to do
#I've adapted this from reading adc values
#on the pico and sending the values to the sd card
#Create a new file (keep this one in case you want that)
#Do the TODOs
from machine import SPI, Pin, ADC
import sdcard, uos
import time

spi = SPI(1,sck=Pin(14), mosi=Pin(15), miso=Pin(12))
cs = Pin(13)
sd = sdcard.SDCard(spi, cs)

uos.mount(sd, '/sd')
print(uos.listdir('/sd'))

print("Starting first write")
#TODO Remove the next line
#adc = ADC(0)
with open('/sd/testData.txt', "w") as f:
    #TODO Remove the while loop we only want to write something
    
    while True:
        #TODO remove the next line
        #x = adc.read_u16() # Replace this line with a sensor reading of your choosing
        t = time.ticks_ms()/1000
        f.write(str(t)) # Write time sample was taken in seconds
        f.write(' ') # A space
        #TODO Remove the next line
        #f.write(str(x)) # Write sample data
        f.write("Some junk")
        f.write('\n') # A new line
        f.flush() # Force writing of buffered data to the SD card
        #TODO Remove the next line
        #print(t, x)
        time.sleep_ms(500)
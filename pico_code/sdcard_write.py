from machine import SPI, Pin, ADC
import sdcard, uos
import time

spi = SPI(1,sck=Pin(14), mosi=Pin(15), miso=Pin(12))
cs = Pin(13)
sd = sdcard.SDCard(spi, cs)

uos.mount(sd, '/sd')
print(uos.listdir('/sd'))

print("Starting first write")

#adc = ADC(0)
with open('/sd/testData.txt', "w") as f:
    while True:
        #x = adc.read_u16() # Replace this line with a sensor reading of your choosing
        t = time.ticks_ms()/1000
        f.write(str(t)) # Write time sample was taken in seconds
        f.write(' ') # A space
        #f.write(str(x)) # Write sample data
        f.write("Some junk")
        f.write('\n') # A new line
        f.flush() # Force writing of buffered data to the SD card
        #print(t, x)
        time.sleep_ms(500)
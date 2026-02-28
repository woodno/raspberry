from machine import SPI, Pin
import sdcard, uos

spi = SPI(1,sck=Pin(14), mosi=Pin(15), miso=Pin(12))
cs = Pin(13)
sd = sdcard.SDCard(spi, cs)

uos.mount(sd, '/sd')
print(uos.listdir('/sd'))
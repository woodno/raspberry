#GPStoSDCardTest
from machine import Pin, UART, SPI
import time
import gps_parser
import sdcard, uos

# Import our GPS parser library
# Set up UART connection to GPS module
#This uart connection is set up from the perspective of the pico
#The TX pin on the GPS unit goes to the RX pin on the pico
#So it goes to the 1 pin
#The RX pin on the GPS unit goes to the TX pin on the pico
#So it goes to the 0 pin
#There are two UARTs, UART0 and UART1. UART0 can be mapped
#to GPIO 0/1, 12/13 and 16/17, and UART1 to GPIO 4/5 and 8/9
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
timestr = str (time.time())
spi = SPI(1,sck=Pin(14), mosi=Pin(15), miso=Pin(12))
cs = Pin(13)
sd = sdcard.SDCard(spi, cs)
# Create a GPS reader object
gps = gps_parser.GPSReader(uart)
output = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
output += "<gpx version=\"1.0\" creator=\"picoExp\" xmlns=\"http://www.topografix.com/GPX/1/0\">\n"
output += "<trk>\n"
output += "<name>Car Track " + timestr + "</name>\n"
output += "<trkseg>\n"
uos.mount(sd, '/sd')
print(uos.listdir('/sd'))
with open('/sd/testData'+timestr+'.txt', "w") as f:
    f.write(output)


i = 0
# Main loop
while i < 30:
    # Get the GPS data, this will also try and read any new information form the GPS
    gps_data = gps.get_data()
    if (gps_data.has_fix):
        i+=1
        dateSplit = gps_data.date.split("/")
        print("Has fix ", gps_data.has_fix, "lat ", gps_data.latitude, "lon ",
          gps_data.longitude, "ele ", gps_data.altitude, "time ", gps_data.time,
          "Date ", gps_data.date, "Speed_Knots ", gps_data.speed_knots  )
        with open('/sd/testData'+timestr+'.txt', "a") as f:
            f.write("<trkpt lat=\""+ str(gps_data.latitude) + "\" lon=\""
                    + str(gps_data.longitude) +"\">\n")
            f.write("<ele>"+ str(gps_data.altitude) + "</ele>\n")
                    
            f.write("<time>" + dateSplit[2] + "-" + dateSplit[1] + "-"
                    + dateSplit[0] + "T" + gps_data.time +"Z</time>\n")
            f.write("</trkpt>\n")
                    
                
           
    # Small delay
    time.sleep(0.5)
    
with open('/sd/testData'+timestr+'.txt', "a") as f:
    f.write ("</trkseg>\n")
    f.write ("</trk>\n")
    f.write ("</gpx>")
    
    

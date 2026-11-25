#Usage
#Two 0.5 sec onboard led blinks tell you the power is on
#Wait till the red GPS module onboard led blinks
#Then you can start recording
#Push and hold the button till you get a 0.1 sec
#Blink on the onboard led
#This tells you the recording to the SDCard has started.
#Before powering off always push and hold the button to end the
#recording and close off the file
#Imports
from machine import Pin, UART, SPI
import time
# This import needs to be put on the pico
# Its found at
# https://github.com/woodno/raspberry/blob/master/pico_code/lib/gps_parser.py
# It needs to go in the lib folder of the pico
import gps_parser
# sdcard import needs to be put on the pico
# Its found at
# https://github.com/woodno/raspberry/blob/master/pico_code/lib/sdcard.py
# It needs to go in the lib folder of the pico
import sdcard, uos
#Used for splitting time string
#Found it did not work on pico.
#import re
#Constants
BUTTON_PIN = 16
PRESSED = 0
NOT_PRESSED = 1
SLEEP_TIME = 0.1

#Set up all the hardware connections
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
led = Pin("LED", Pin.OUT) # Set up the onboard LED

#Let us know the power is on with 2 blinks
led.value(True)
time.sleep(0.5)
led.value(False)
time.sleep(0.5)
led.value(True)
time.sleep(0.5)
led.value(False)


#Set up the uart connection between the GPS module and the pico
#This uart connection is set up from the perspective of the pico
#The TX pin on the GPS unit goes to the RX pin on the pico
#So it goes to the 1 pin
#The RX pin on the GPS unit goes to the TX pin on the pico
#So it goes to the 0 pin
#There are two UARTs, UART0 and UART1. UART0 can be mapped
#to GPIO 0/1, 12/13 and 16/17, and UART1 to GPIO 4/5 and 8/9
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
# Create a GPS reader object
gps = gps_parser.GPSReader(uart)
#Set up the SD Card connections
#The master in this case is the pico.
#So the pin 15 on the pico goes to the mosi pin on the sdcard module
spi = SPI(1,sck=Pin(14), mosi=Pin(15), miso=Pin(12))
cs = Pin(13)
sd = sdcard.SDCard(spi, cs)
uos.mount(sd, '/sd')

#TODO Set the Real Time Clock to the correct time and date to
# Get the correct modified date on the file
#Use code in SetPicoClock.py
#Hold off the initialization until a datetime has been
#picked up from the gps
def initilizeFile(): 
    timeStr = str (time.time())
    output = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    output += "<gpx version=\"1.1\" creator=\"U3ANoel\" xmlns=\"http://www.topografix.com/GPX/1/1\"\n"
    output += "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\n"
    output += "xsi:schemaLocation=\"http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd\">\n"
    output += "<trk>\n"
    output += "<name>Record Track " + timeStr + "</name>\n"
    output += "<trkseg>\n"
    with open('/sd/testData'+timeStr+'.gpx', "w") as f:
        f.write(output)
    return timeStr

def recordTrackPoint(timeStr):
    gps_data = gps.get_data()
    if (gps_data.has_fix):
        dateSplit = gps_data.date.split("/")
        print("Has fix ", gps_data.has_fix, "lat ", gps_data.latitude, "lon ",
          gps_data.longitude, "ele ", gps_data.altitude, "time ", gps_data.time,
          "Date ", gps_data.date, "Speed_Knots ", gps_data.speed_knots  )
        with open('/sd/testData'+timeStr+'.gpx', "a") as f:
            f.write("<trkpt lat=\""+ str(gps_data.latitude) + "\" lon=\""
                    + str(gps_data.longitude) +"\">\n")
            f.write("<ele>"+ str(gps_data.altitude) + "</ele>\n")
                    
            f.write("<time>" + dateSplit[2] + "-" + dateSplit[1] + "-"
                    + dateSplit[0] + "T" + gps_data.time +"Z</time>\n")
            f.write("</trkpt>\n")
def closeFile(timeStr):
    with open('/sd/testData'+timeStr+'.gpx', "a") as f:
        f.write ("</trkseg>\n")
        f.write ("</trk>\n")
        f.write ("</gpx>")
    

isRecording = False
#is one unit of blinking
isLedOn = False


isTriggerReset = True
#TODO Set a variable to hold when the
#first fix is achieved
isFirstGPSFixReceived = False
while not isFirstGPSFixReceived:
    gps_data = gps.get_data()
    if (gps_data.has_fix):
        isFirstGPSFixReceived = True
        dateSplit = gps_data.date.split("/")
        timeSplit = gps_data.time.split(".")
        timeSplitHMS = timeSplit[0].split(":")
        #timeSplit = re.split(r"[:.]", gps_data.time)
        rtc = machine.RTC()
        # Format:tuple of (year, month, day, weekday, hours, minutes, seconds, subseconds)
# #         print ("int(dateSplit[2])",int(dateSplit[2]))
# #         print("int(dateSplit[1])",int(dateSplit[1]))
# #         print("int(dateSplit[0])",int(dateSplit[0]))
# #         print("int(timeSplitHMS[0])",int(timeSplitHMS[0]))
# #         print("int(timeSplitHMS[1])",int(timeSplitHMS[1]))
# #         print("int(timeSplitHMS[2])", int(timeSplitHMS[2]))
        rtc.datetime((int(dateSplit[2]), int(dateSplit[1]), int(dateSplit[0]), 0,
                      int(timeSplitHMS[0]), int(timeSplitHMS[1]), int(timeSplitHMS[2]), 0))
    time.sleep(SLEEP_TIME)
    print("no fix yet")
print ("fix done")
try:
    while True:
            
        if button.value() == NOT_PRESSED:
            isTriggerReset = True
        #isTriggerReset pevents one
        #push of the switch being
        #recorded as multipe toggles.
        if button.value() == PRESSED and isTriggerReset:
            isRecording = not isRecording
            isTriggerReset = False
            if isRecording:
                #Not really needed
                #Led would blink on second run
                isLedOn = True
                timeStr = initilizeFile()
            else:
                #makes sure led is left in an off state
                led.value(0)
                closeFile(timeStr)
        
        if isRecording:
            led.value(isLedOn)  # Turn the LED ON
            recordTrackPoint(timeStr)
            isLedOn = not isLedOn
        
            
            
            
        time.sleep(SLEEP_TIME) 

finally:
	led.value(0)
	led = Pin("LED", Pin.IN) 


"""
Lego Car code
Written by Noel Wood and U3A students
Some code taken from code written @ Core Electronics
Some code adapted from examples in: https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf
    - Version 1.0 Mar 2026

"""

#import list
import time
import network
import machine
import uasyncio as asyncio
from machine import Pin, PWM, SPI, UART
from umqtt.simple import MQTTClient
import json
import sdcard, uos
import gps_parser

#Constant List
#Do not adjust this to a faster wait time without checking ToS
#The terms of service as of Mar 2026 state you are allowed
#To publish once every 2 seconds
MIN_ADAFRUIT_PUBLISH_WAIT = 2

#global variable list
check_interval_sec = 0.25
isGpsRecordingOn = False



#HardwareDefn
led = Pin("LED", Pin.OUT)
wlan = network.WLAN(network.STA_IF)
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
spi = SPI(1,sck=Pin(14), mosi=Pin(15), miso=Pin(12))
cs = Pin(13)
sd = sdcard.SDCard(spi, cs)
uos.mount(sd, '/sd')
pwm_enable_drive_motor = PWM(Pin(3))
pwm_enable_drive_motor.freq(1000)
pwm_enable_servo = PWM(Pin(10))
pwm_enable_servo.freq(1150)
input1_pin = Pin(4, Pin.OUT)
input2_pin = Pin(5, Pin.OUT)
c1 = Pin(6, Pin.OUT)
c2 = Pin(7, Pin.OUT)

#function blink_led to communicate status with user
def blink_led(frequency = 0.5, num_blinks = 3):
    for _ in range(num_blinks):
        led.on()
        time.sleep(frequency)
        led.off()
        time.sleep(frequency)

#bring in connection file
#todo connect the following mqtt topics 
#"mqtt_gpsrecording_topic"
#"mqtt_speed_topic"
def read_connection_file():
    with open("passwordFile.pwd") as f:
        x = json.loads(f.read())
    print(json.dumps(x))
    global wifi_ssid 
    global wifi_password
    global mqtt_host
    global mqtt_username
    global mqtt_password
    global mqtt_direction_topic
    global mqtt_leftright_topic
    wifi_ssid = x["wifi_ssid"]
    wifi_password = x["wifi_password"]
    # Fill in your Adafruit IO Authentication and Feed MQTT Topic details
    mqtt_host = x["mqtt_host"]
    mqtt_username = x["mqtt_username"]  # Your Adafruit IO username
    mqtt_password = x["mqtt_password"]  # Adafruit IO Key
    mqtt_direction_topic = x["mqtt_direction_topic"]  # The MQTT topic for your Adafruit IO Feed
    mqtt_leftright_topic = x["mqtt_leftright_topic"]

#async Function to connect to wifi
def connect_to_wifi():
    wlan.active(True)
    wlan.config(pm = 0xa11140)  # Diable powersave mode
    wlan.connect(wifi_ssid, wifi_password)

    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)

    #Reports connection error trough blinking light
    if wlan.status() != 3:
        blink_led(0.1, 10)
        raise RuntimeError('WiFi connection failed')
    else:
        blink_led(0.5, 2)
        print('connected')
        status = wlan.ifconfig()
        print('ip = ' + status[0])



#todo finish function to publish initial state conditions
#this in place before the car starts working
async def publishInitialStates(mqtt_client):
    print("At Publish Initial State")
    #todo Below are the initial states I want to publish
    # isCarDirectionForward = False
    # carLeftRight = 50
    # carSpeed = 0
    # isGPSRecordingOn = False
    #todo test that an integer can be set as an mqtt message
    await publishTopic (mqtt_client, mqtt_direction_topic, "Fwd")
    isCarDirectionForward = True
    await publishTopic (mqtt_client, mqtt_leftright_topic, b'50')
    carLeftRight = 50
#todo implement setCarInitialStates
async def setCarInitialStates():
    print("todo")
#todo implement setCarSpeed    
async def setCarSpeed(speed):
    print("todo")
#todo setCarDirection
async def setCarDirection(isCarForward):
    print("todo")
#todo implement setCarLeftRight
async def setCarLeftRight(carLeftRight):
    print("todo")

async def setIsGPSRecordingOn (isOn):
    global isGpsRecordingOn
    if not isGpsRecordingOn and isOn :
        initializeGPXFile()
        isGpsRecordingOn = True
    if isGpsRecordingOn and not isOn :
        saveClosingPartOfGPX()
        isGpsRecordingOn = False
        
    print("todo")
    #todo return IsGPSRecordingOn value
#todo implement initializeGPXFile
#put in all of the data up to the trackpoint element 
async def initializeGPXFile ():
    print("todo")
    #todo return filename object
#todo implement saveTrackPointElement
async def saveTrackPointElement(lat, lon, ele, time, date):
    print("todo")
#todo implement saveClosingPartOfGPX
async def saveClosingPartOfGPX():
    print("todo")



async def publishTopic (mqtt_client, topic, msg):
    mqtt_client.publish(topic, msg)
    #Do not adjust this to a faster wait time
    #The terms of service as of Mar 2026 state you are allowed
    #To publish once every 2 seconds
    await asyncio.sleep(MIN_ADAFRUIT_PUBLISH_WAIT)



#callback function to wait for subscribed messages
def mqtt_callback(topic, msg):
    print(f"Received: {msg} on {topic}")
    #todo test how to handle callbacks on differnt topics
    #todo handle different calls on different topics
    #todo work out how to turn byte literals into ints and strings

#todo implement handleChangeOfSpeed
async def handleChangeOfSpeed(newSpeed):
    print(f"At handleChangeOfSpeed with new speed ",newSpeed)

#todo implement handleChangeOfLeftRight
#todo make sure to put the car back to middle direction after async wait 0.5 seconds
#todo make sure to publish the mqtt setting back to the middle after async wait 0.5 seconds  
async def handleChangeOfLeftRight(newLeftRight):
    print(f"At handleChangeOfSpeed with new LeftRight ",newLeftRight)

#todo implement handleChangeOfDirection
async def handleChangeOfDirection(newDirection):
    print(f"At handleChangeOfSpeed with new Direction ",newDirection)

#todo implement handleStartGpsFile()
async def handleStartGpsFile():
    print("At handleStartGpsFile")
    
#todo implement handleStopGpsFile()
async def handleStopGpsFile():
    print("At handleStopGpsFile")   


        
async def main():
    print("Reading connection settings")
    read_connection_file()
    print('Connecting to WiFi...')
    
    connect_to_wifi()
    mqtt_client_id = machine.unique_id().hex()
    mqtt_client = MQTTClient(
        client_id=mqtt_client_id,
        server=mqtt_host,
        user=mqtt_username,
        password=mqtt_password)
    print("before mqtt connect")
    mqtt_client.connect()
    mqtt_client.set_callback(mqtt_callback)
    mqtt_client.subscribe(mqtt_direction_topic)
    mqtt_client.subscribe(mqtt_leftright_topic)
    print("after mqtt connect")
    await publishInitialStates(mqtt_client)
    await setLegoCarInitialStates()
    
    #Check for gps data
    gps = gps_parser.GPSReader(uart)
    while True:
        
        mqtt_client.wait_msg()
        
        
        gps_data = gps.get_data()
         
        #todo if we are told via a mqtt message to generate a gps file
        #todo Initialize the gpx file and never call it again till a second file is required
        #todo check if we have a fix and record a trackpoint if we do
        #todo close off the file if the mqtt topic is toggled
        #todo repopen a new file it it is toggled again
#         if gps_data.has_fix:
#             asyncio.create_task(todo put in the create trackpoint task here)
# 
#                          
#          else:
#              print ("No GPS fix available")
         
        await asyncio.sleep(check_interval_sec)

        #time.sleep(0.1)

    
    
    
#set main to run
try:
    asyncio.run(main())
finally:
    print("Finished")
    #todo reset all the pwm and out pins to in pins
    #Im not sure this actually will do anything with a battery paower
    #pack because it will just turn off without going here.
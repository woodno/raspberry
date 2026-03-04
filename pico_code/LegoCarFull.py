"""
Lego Car code
Written by Noel Wood
Taken from cade written @ Core Electronics
Adapted from examples in: https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf
    - Version 1.0 Mar 2026

Controls 1) a lego car using mqtt Two motors a servo and a normal drive motor
2) Gets GPS data from a GPS module on the car and logs it using mqtt and an SD card module


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


#constant list
check_interval_sec = 0.25


#HardwareDefn
led = Pin("LED", Pin.OUT)
wlan = network.WLAN(network.STA_IF)
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
spi = SPI(1,sck=Pin(14), mosi=Pin(15), miso=Pin(12))
cs = Pin(13)
sd = sdcard.SDCard(spi, cs)
uos.mount(sd, '/sd')

#function blink_led to communicate status with user
def blink_led(frequency = 0.5, num_blinks = 3):
    for _ in range(num_blinks):
        led.on()
        time.sleep(frequency)
        led.off()
        time.sleep(frequency)

#bring in connection file
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

    # Handle connection error
    if wlan.status() != 3:
        blink_led(0.1, 10)
        raise RuntimeError('WiFi connection failed')
    else:
        blink_led(0.5, 2)
        print('connected')
        status = wlan.ifconfig()
        print('ip = ' + status[0])

#async function to set up clients

#async function to publish initial state conditions
        
async def save_to_sd(latitude, longitude):
    with open('/sd/testData.txt', "w") as f:
        t = time.ticks_ms()/1000
        f.write(str(t)) # Write time sample was taken in seconds
        f.write(' ') # A space
        #f.write(str(x)) # Write sample data
        f.write(str(latitude) + "," + str(longitude) )
        f.write('\n') # A new line
        f.flush() # Force writing of buffered data to the SD card
        print ("Wrote " + str(latitude) + "," + str(longitude) + " to sd card")

#callback function to wait for subscribed messages
def mqtt_callback(topic, msg):
    print(f"Received: {msg} on {topic}")
        
#async function to publish gps data
#async def write_gps_data():
    
#async function to store data on sdcard

#async main function
        
async def main():
    print("Reading connection settings")
    read_connection_file()
    print('Connecting to WiFi...')
    
    connect_to_wifi()
    #mqtt_client_id = machine.unique_id().hex()
    mqtt_client_id = "qwerafshdndhsnbhdebf"
    mqtt_client1 = MQTTClient(
        client_id=mqtt_client_id,
        server=mqtt_host,
        user=mqtt_username,
        password=mqtt_password)
    
    #mqtt_client_id = machine.unique_id().hex()
    mqtt_client_id = "dhcjhbwfbwifnjkwfnh"
    mqtt_client2 = MQTTClient(
        client_id=mqtt_client_id,
        server=mqtt_host,
        user=mqtt_username,
        password=mqtt_password)
    mqtt_client1.set_callback(mqtt_callback)
    mqtt_client2.set_callback(mqtt_callback)
    mqtt_client1.connect()
    mqtt_client2.connect()
    mqtt_client1.subscribe(mqtt_direction_topic)
    mqtt_client2.subscribe(mqtt_leftright_topic)
    #Check for gps data
    gps = gps_parser.GPSReader(uart)
    while True:
        mqtt_client1.check_msg()
        mqtt_client2.check_msg()
        
        gps_data = gps.get_data()
        if gps_data.has_fix:
            print ("latlog:",str(gps_data.latitude), gps_data.longitude)
            asyncio.create_task(save_to_sd( gps_data.latitude, gps_data.longitude))
        else:
            print ("No GPS fix available")
        # Perform other tasks
        
        await asyncio.sleep(check_interval_sec)

        #time.sleep(0.1)

    
    
    
#set main to run
try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()        
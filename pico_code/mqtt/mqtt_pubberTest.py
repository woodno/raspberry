"""
A simple example that connects to the Adafruit IO MQTT server
and publishes a text and a number to two different feeds 
"""

import network
import time
from math import sin
from umqtt.simple import MQTTClient
import json
# Fill in your WiFi network name (ssid) and password here:
with open("passwordFile.pwd") as f:
    x = json.loads(f.read())
print(json.dumps(x))
wifi_ssid = x["wifi_ssid"]
wifi_password = x["wifi_password"]
# Fill in your Adafruit IO Authentication and Feed MQTT Topic details
mqtt_host = x["mqtt_host"]
mqtt_username = x["mqtt_username"]  # Your Adafruit IO username
mqtt_password = x["mqtt_password"]  # Adafruit IO Key
mqtt_direction_topic = x["mqtt_direction_topic"]  # The MQTT topic for your Adafruit IO Feed

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_password)
while wlan.isconnected() == False:
    print('Waiting for connection...')
    time.sleep(1)
print("Connected to WiFi")





# Enter a random ID for this MQTT Client
# It needs to be globally unique across all of Adafruit IO.
mqtt_client_id = "somethingreallyrandomandunique123"

# Initialize our MQTTClient and connect to the MQTT server
mqtt_client = MQTTClient(
        client_id=mqtt_client_id,
        server=mqtt_host,
        user=mqtt_username,
        password=mqtt_password)

mqtt_client.connect()

# Publish a data point to the Adafruit IO MQTT server every 3 seconds
# Note: Adafruit IO has rate limits in place, every 3 seconds is frequent
#  enough to see data in realtime without exceeding the rate limit.
counter = 0
try:
    while counter < 20:
        print ("Publish Fwd")
        mqtt_client.publish(mqtt_direction_topic, "Fwd")
        
        # Delay a bit to avoid hitting the rate limit
        time.sleep(3)
        print ("Publish Bkw")
        mqtt_client.publish(mqtt_direction_topic, "Bkw")
        
        # Delay a bit to avoid hitting the rate limit
        time.sleep(3)
        counter+=1
except Exception as e:
    print(f'Failed to publish message: {e}')
finally:
    mqtt_client.disconnect()
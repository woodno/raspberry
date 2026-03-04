#Simple multiple mqtt clients
from umqtt.simple import MQTTClient
import time

# Define client settings
broker = "broker.hivemq.com"
client1 = MQTTClient("client_1", broker)
client2 = MQTTClient("client_2", broker)

# Callback
def sub_cb(topic, msg):
    print(f"Received: {msg} on {topic}")

# Setup Clients
client1.set_callback(sub_cb)
client2.set_callback(sub_cb)
client1.connect()
client2.connect()
client1.subscribe(b"topic/1")
client2.subscribe(b"topic/2")

# Main Loop
while True:
    client1.check_msg()
    client2.check_msg()
    # Perform other tasks
    time.sleep(0.1)

import uasyncio as asyncio
from umqtt.simple import MQTTClient
import uuid
client_id = str(uuid.uuid4())

# Asynchronous check function
async def mqtt_loop(client, topic):
    client.connect()
    client.subscribe(topic)
    while True:
        client.check_msg()
        await asyncio.sleep(0.1) # Non-blocking sleep

async def main():
    broker = "broker.hivemq.com"
    c1 = MQTTClient("client_1", broker)
    c2 = MQTTClient("client_2", broker)
    
    # Run both clients concurrently
    await asyncio.gather(
        mqtt_loop(c1, b"topic/1"), mqtt_loop(c2, b"topic/2")
    )

# Start the event loop
# asyncio.run(main()) # In newer MicroPython

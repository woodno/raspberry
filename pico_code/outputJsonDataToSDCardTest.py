import machine
import sdcard
import os
import json
import time

# 1. Setup SPI and SD Card
# Use SPI1, pins 10, 11, 12
spi = machine.SPI(1, baudrate=1000000, polarity=0, phase=0,
                  sck=machine.Pin(10), mosi=machine.Pin(11), miso=machine.Pin(12))
cs = machine.Pin(13, machine.Pin.OUT)

# Initialize SD Card
sd = sdcard.SDCard(spi, cs)
# Mount Filesystem
vfs = os.VfsFat(sd)
os.mount(vfs, "/sd")

# 2. Prepare JSON Data
data = {
    "timestamp": time.time(),
    "temperature": 25.5,
    "status": "active"
}
json_string = json.dumps(data) # Convert dict to JSON string

# 3. Write/Append JSON to SD Card
print("Writing to SD card...")
with open("/sd/data.json", "a") as f:
    f.write(json_string + "\n") # Write as a new line
print("Log Saved: ", json_string)

# 4. Unmount (Optional, good for safe removal)
# os.umount("/sd")

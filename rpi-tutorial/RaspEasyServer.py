# RaspiEasyServer.py

from tcpcom import TCPServer
import time
import RPi.GPIO as GPIO
import smbus

P_BUTTON = 12 # Button A
dt = 0.1  # Measurement period
port = 5000 # IP port

def onStateChanged(state, msg):
    if state == "LISTENING":
        print "Server:-- Listening..."
    elif state == "CONNECTED":
        print "Server:-- Connected to", msg

def readData(port = 0):
    if port == 0:
        adc_address = 0x48
    elif port == 1:    
        adc_address = 0x4D
    rd = bus.read_word_data(adc_address, 0)
    data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
    data = data >> 2
    return data

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN)

print "starting..."
setup()
bus = smbus.SMBus(1) 
server = TCPServer(port, stateChanged = onStateChanged)
while GPIO.input(P_BUTTON) == GPIO.LOW:
    if server.isConnected():
        v = readData()
        server.sendMessage(str(v))
        time.sleep(dt)
server.terminate()
print "Server terminated"
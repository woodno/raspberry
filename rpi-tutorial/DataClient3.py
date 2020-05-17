# DataClient3.py

from tcpcom import TCPClient
import time
import RPi.GPIO as GPIO

IP_ADDRESS = "192.168.0.111"
#IP_ADDRESS = "5.149.19.200"
#IP_ADDRESS = "raplu.zapto.org"
IP_PORT = 22000
P_BUTTON = 24 # adapt to your wiring

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN, GPIO.PUD_UP)

def onStateChanged(state, msg):
    global isConnected
    if state == "CONNECTING":
       print "Client:-- Waiting for connection..."
    elif state == "CONNECTED":
       print "Client:-- Connection estabished."
    elif state == "DISCONNECTED":
       print "Client:-- Connection lost."
       isConnected = False
    elif state == "MESSAGE":
       print "Client:-- Received data:", msg

setup()
client = TCPClient(IP_ADDRESS, IP_PORT, stateChanged = onStateChanged)
rc = client.connect()
if rc:
    isConnected = True
    while isConnected:
        if GPIO.input(P_BUTTON) == GPIO.LOW:
            reply = "Button pressed"
        else:
            reply = "Button released"
        client.sendMessage(reply)
        print "Client:-- Sending message:", reply
        time.sleep(2)
    print "Done"    
else:
    print "Client:-- Connection failed"      
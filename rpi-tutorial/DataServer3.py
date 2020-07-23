# DataServer3.py

from tcpcom import TCPServer

IP_PORT = 22000

def onStateChanged(state, msg):
    if state == "LISTENING":
        print "Server:-- Listening..."
    elif state == "CONNECTED":
        print "Server:-- Connected to", msg
    elif state == "MESSAGE":
        print "Server:-- Message received:", msg

server = TCPServer(IP_PORT, stateChanged = onStateChanged)
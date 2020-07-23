# RaspEasyClientGraph.py

from tcpcom import TCPClient
from gpanel import *
import time

def onStateChanged(state, msg):
    global t
    if state == "CONNECTING":
       title("Waiting for connection...")
    elif state == "CONNECTED":
       title("Connection estabished.")
    elif state == "MESSAGE":
        data = int(msg)
        if t == 0:
            move(t, data)
        else:
            draw(t, data)
        t += 0.1
        if t > 10:
            time.sleep(100)
            clear()
            drawGrid(0, 10, 0, 1000)

def onExit():
    client.disconnect()
    dispose()
    
port = 5000 # IP port
host = "192.168.1.106"
makeGPanel(-1, 11, -100, 1100)
drawGrid(0, 10, 0, 1000, "gray")
addExitListener(onExit)
t = 0
client = TCPClient(host, port, stateChanged = onStateChanged)
rc = client.connect()
if not rc:
    title("Connection failed")
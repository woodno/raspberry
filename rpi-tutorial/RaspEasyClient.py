# RaspEasyClient.pc

from tcpcom import TCPClient
#from easygui import msgbox, enterbox

def onStateChanged(state, msg):
    if state == "CONNECTING":
       print "Client:-- Waiting for connection..."
    elif state == "CONNECTED":
       print "Client:-- Connection estabished."
    elif state == "MESSAGE":
       print "Client:-- Received data:", msg

port = 5000 # IP port
host = "192.168.1.106"
client = TCPClient(host, port, stateChanged = onStateChanged)
rc = client.connect()
if rc:
    msgDlg("OK to terminate")  # TigerJython
#    msgbox("Button client running. OK to stop","Button Client")
    client.disconnect()

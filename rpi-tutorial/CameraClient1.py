# CameraClient1.py
# Display image in TigerJython's GPanel graphics window

from threading import Thread
import socket, time
from gpanel import *

VERBOSE = False
IP_ADDRESS = "192.168.0.12"
IP_PORT = 22000

def debug(text):
    if VERBOSE:
        print "Debug:---", text

# --------------------- class Receiver ---------------------------
class Receiver(Thread):
    def run(self):
        debug("Receiver thread started")
        while True:
            try:
                rxData = self.readServerData()
            except:    
                debug("Exception in Receiver.run()")
                isReceiverRunning = False
                closeConnection()
                break
        debug("Receiver thread terminated")

    def readServerData(self):
        global isJPEG
        debug("Calling readResponse")
        bufSize = 4096
        data = ""
        while data[-2:] != "\xff\xd9":
        # eof tag for jpeg files (both chars must be in same block)
        # We are not sure 100% that this sequence is never embedded in image
        # but it is improbable to happen at the end of the data block
            try:
                blk = sock.recv(bufSize)
                if blk != None:
                    debug("Received data block, len: " + str(len(blk)))
                else:
                    debug("sock.recv() returned with None")
            except:
                raise Exception("Exception from blocking sock.recv()")
            data += blk
            print "JPEG received. Displaying it..."
            display(data)
# -------------------- End of Receiver ---------------------

def startReceiver():
    debug("Starting Receiver thread")
    receiver = Receiver()
    receiver.start()

def sendCommand(cmd):
    debug("sendCommand() with cmd = " + cmd)
    try:
        sock.sendall(cmd)
    except:
        debug("Exception in sendCommand()")
        closeConnection()

def closeConnection():
    debug("Closing socket")
    sock.close()

def connect():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    debug("Connecting...")
    try:
        sock.connect((IP_ADDRESS, IP_PORT))
    except:
        debug("Connection failed.")
        return False
    startReceiver()
    return True
 
def display(data):
    img = readImage(data)
    if img != None:
        image(img, 0, 0)   

def onExit():
    global isRunning
    isRunning = False
    dispose()

width = 640
height = 480
makeGPanel(Size(width, height))  
addExitListener(onExit)
sock = None
isRunning = True   

if connect():
    print "Connection established"
    time.sleep(1)
    while isRunning:
        print "Sending command 'go'..."
        sendCommand("go")
        time.sleep(2)
    print "Disconnecting now..."    
#    sendCommand("disconnect")    
    closeConnection()
else:
    print "Connection to %s:%d failed" %(IP_ADDRESS, IP_PORT)
print "done"    
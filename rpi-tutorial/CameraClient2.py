# CameraClient2.py
# Save image to disk and display it in standard viewer

from threading import Thread
import socket, time
import webbrowser

VERBOSE = False
IP_ADDRESS = "192.168.0.12"
IP_PORT = 22000
RECEIVER_TIMEOUT = 5  # seconds

def debug(text):
    if VERBOSE:
        print "Debug:---", text

# -------------------------------- class Receiver ---------------------------
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
        debug("Calling readResponse")
        bufSize = 4096
        data = ""
        while data[-2:] != "\xff\xd9":
            # eof tag for jpeg files,
            # we are not sure 100% that this sequence is never embedded in image
            # but it is very improbable to fit the last two bytes of the 4096 size block
            try:
                blk = sock.recv(bufSize)
                if blk != None:
                    debug("Received data block from server, len: " + str(len(blk)))
                else:
                    debug("sock.recv() returned with None")
            except:
                raise Exception("Exception from blocking sock.recv()")
            data += blk
        print "JPEG received. Displaying it..."
        display(data)
# ------------------------ End of Receiver ---------------------

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

def saveData(data, filename):
    file = open(filename, "wb")
    file.write(data)
    file.close()

def display(data):
    jpgFile = "c:/scratch/test.jpg"
    saveData(data, jpgFile)
    webbrowser.open(jpgFile)

width = 640
height = 480
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
    sendCommand("disconnect")
# closeConnection()
else:
    print "Connection to %s:%d failed" % (IP_ADDRESS, IP_PORT)
print "done"    
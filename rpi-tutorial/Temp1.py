# Temp1.py

import time
from py7seg import Py7Seg # xxx

masterFolder = "/sys/devices/w1_bus_master1/"

def getSlaveFolders():
    # Get list of all 1-wire slave folders
    file = open(masterFolder + "w1_master_slaves")
    slaveFolders = file.read().splitlines()
    file.close()
    return slaveFolders

def getTemperature(slaveFolder):
      # Read content of corresponding w1_slave file. Format:
      # 6f 01 4b 46 7f ff 01 10 67 : crc=67 YES
      # 6f 01 4b 46 7f ff 01 10 67 t=22937
      file = open(masterFolder + slaveFolder + '/w1_slave')
      lines = file.read().splitlines()
      file.close()
    
      # Extract temperature from second line
      temperature = float(lines[1][29:]) / 1000
      return temperature

ps = Py7Seg() # xxx
slaveFolders = getSlaveFolders()
while True:
    # Extract temperature from first slave
    temp = getTemperature(slaveFolders[0])
    print("T = %6.2f deg" %temp)
    w = "%4.1f" %temp
    ps.showText(w[0] + w[1] + w[3] + '#', dp = [0, 1, 0]) # xxx    
    time.sleep(1)
# Display4d.py

from OLED1306 import OLED1306
import time
from subprocess import Popen, PIPE
import re


def getIPAddresses():
    '''
    @return:  List of all IP addresses of machine
    '''
    p = Popen(["ifconfig"], stdout = PIPE)
    ifc_resp = p.communicate()
    patt = re.compile(r'inet\s*\w*\S*:\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    resp = patt.findall(ifc_resp[0])
    return resp

disp = OLED1306()
disp.setFontSize(18)
disp.println("IP Address(es):")
for address in getIPAddresses():
    if address != '127.0.0.1':
       disp.println(address)

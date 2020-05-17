# py7seg.py

'''
Class that represents a 4 digit 7-segment display using the SAA1064 chip
Source of supply: Ebay or www.elv.de (order # 105697)

 This software is part of the raspibrick module.
 It is Open Source Free Software, so you may
 - run the code for any purpose
 - study how the code works and adapt it to your needs
 - integrate all or parts of the code in your own programs
 - redistribute copies of the code777
 - improve the code and release your improvements to the public
 However the use of the code is entirely your responsibility.
 '''

from smbus import *
import RPi.GPIO as GPIO
from threading import Thread
import time

class SMBusException(Exception): pass


# ------------------- class Py7Seg ----------------------
class Py7Seg():
    '''
    Abstraction of the 4 digit 7-segment display based on the SAA1064 display driver.
    If no display is found, all display methods return immediately. The static variable SharedConstants.PATTERN defines a dictionary
    that maps ASCII characters to display patterns and can be modified by the user program.

    Default:

    The 7 segments have the following binary weights
           1
           -
     32 |     |2

          64
           -
     16 |     |4
           -
           8

   The decimal points has weight 128.

    '''

    DEBUG = False
    VERSION = "1.00 - April 2016"

    '''
    Character to binary value mapping for 4 digit 7 segment display
    '''
    PATTERN = {' ': 0, '!': 134, '"': 34, '#': 99, '$': 0, '%': 0, '&': 0, '\'':  2, '(': 0, ')': 0,
           '*': 0, '+': 0, ',': 4, '-': 64, '.': 128, '/': 82, '0': 63, '1': 6, '2': 91, '3': 79,
           '4': 102, '5': 109, '6': 125, '7': 7, '8': 127, '9': 111, ':': 0, ';': 0, '<': 0,
           '=': 72, '>': 0, '?': 0, '@': 93, 'A': 119, 'B': 124, 'C': 57, 'D': 94, 'E': 121,
           'F': 113, 'G': 61, 'H': 118, 'I': 48, 'J': 14, 'K': 112, 'L': 56, 'M': 85, 'N': 84,
           'O': 63, 'P': 115, 'Q': 103, 'R': 80, 'S': 45, 'T': 120, 'U': 62, 'V': 54, 'W': 106,
           'X': 73, 'Y': 110, 'Z': 27, '[': 57, '\\':  100, ']': 15, '^': 35, '_': 8, '`': 32,
           'a': 119, 'b': 124, 'c': 88, 'd': 94, 'e': 121, 'f': 113, 'g': 61, 'h': 116, 'i': 16,
           'j': 12, 'k': 112, 'l': 48, 'm': 85, 'n': 84, 'o': 92, 'p': 115, 'q': 103, 'r': 80, 's': 45,
           't': 120, 'u': 28, 'v': 54, 'w': 106, 'x': 73, 'y': 110, 'z': 27, '{': 0, '|': 48, '}': 0, '~': 65}

    # ----------------------- static methods ---------------------
    @staticmethod
    def debug(msg):
        if Py7Seg.DEBUG:
            print "Py7Seg debug->", msg

    @staticmethod
    def getVersion():
        return Py7Seg.VERSION

    @staticmethod
    def getDisplayableChars():
        '''
        Returns a string with all displayable characters taken from PATTERN dictionary.
        @return: The character set that can be displayed
        '''
        s = "<SPACE>"
        k = 33
        while k < 127:
            ch = chr(k)
            if Py7Seg.PATTERN[ch] != 0:
                s = s + ch
            k += 1
        return  s

    @staticmethod
    def toHex(intValue):
        '''
        Returns a string with hex digits from given number (>0, any size).
        @param number: the number to convert (must be positive)
        @return: string of hex digits (uppercase), e.g. 0xFE
        '''
        return '%02x' % intValue

    @staticmethod
    def toBytes(intValue):
        '''
        Returns a list of four byte values [byte#24-#31, byte#16-#23, byte#8-#15, byte#0-#7] of given integer.
        @param number: an integer
        @return: list with integers of 4 bytes [MSB,..., LSB]
        '''
        byte0 = intValue & 0xff
        byte1 = (intValue >> 8) & 0xff
        byte2 = (intValue >> 16) & 0xff
        byte3 = (intValue >> 24) & 0xff
        return [byte3, byte2, byte1, byte0]

    @staticmethod
    def toInt(hexValue):
        '''
        Returns an integer from given hex string
        @param number: a string with the number to convert, e.g. "FE" or "fe" or "0xFE" or "0XFE"
        @return: integer number
        '''
        return int(hexValue, 16)

    @staticmethod
    def delay(timeout):
        time.sleep(timeout / 1000.0)

    # ----------------------- Constructor ------------------------
    def __init__(self, i2c_address = 0x38):
        '''
        Creates a display instance with display set to given i2c address (default: 0x38).
        The display is NOT cleared. It is set to the lowest brightness level 1 (4 mA).
        @param i2c_address: the i2c address (default: 0x38)
        '''
        self.i2c_address = i2c_address
        self._bus = None
        self._isReady = True
        self._tickerThread = None
        self._blinkerThread = None

        try:
            if GPIO.RPI_REVISION > 1:
                self._bus = SMBus(1) # For revision 2 Raspberry Pi
                Py7Seg.debug("I2C at bus 1 detected")
            else:
                self._bus = SMBus(0) # For revision 1 Raspberry Pi
                Py7Seg.debug("I2C at bus 0 detected")
        except:
            Py7Seg.debug("Failed to detect I2C bus.")

        if self._isReady:
            self._startPos = -1  # no text yet
            self.setBrightness(1)

    # ----------------------- Methods ----------------------
    def setBrightness(self, brightness):
        '''
        Sets the brightness of the display.
        @param luminosity the brightness (0..7, 0: invisible)
        '''
        instruction_byte = 0x00
        if brightness < 0:
            brightness = 0
        if brightness > 7:
            brightness = 7
        control_byte = 7 + (brightness << 4)    
        
        # control_byte = 0b00010111 
        # b0 = 1: dynamic mode (autoincrement digits)  
        # b1 = 1: digit 1/3 not blanked, b2 = 1: digit 2/4 not blanked
        # b4 = 1: 3 mA segment current 
        # write to control register
        self._bus.write_byte_data(self.i2c_address, instruction_byte, control_byte)

    def writeData(self, data):
        '''
        Sends 4 data bytes to the display
        @param data list or tuple of integers whose lower byte are used (higher bytes
        are ignored).
        '''
        if not self._isReady:
            return
        if not (type(data) == list or type(data) == tuple)  or len(data) != 4:
            raise Exception("Error in Py7Seg.writeData():\nWrong parameter type.")
        for v in data:
            if not (type(v) == int):
                raise Exception("Error in Py7Seg.writeData():\nWrong parameter type.")
        try:
            cmd = 1 # start with digit 1
            Py7Seg.debug("bus.write_i2c_block_data(" + str(self.i2c_address) + "," + str(cmd) + "," + str(data) + ")")
            self._bus.write_i2c_block_data(self.i2c_address, cmd, data)
        except IOError, err:
            raise Exception("Py7Seg.writeData(). Can't access device at address 0x%02X" % self.i2c_address)

    def clear(self):
        '''
        Clears the display (all digits are turned off).
        '''
        Py7Seg.debug("Calling clear()")
        if not self._isReady:
            return
        self._bus.write_i2c_block_data(self.i2c_address, 1, [0, 0, 0, 0])

    def showText(self, text, pos = 0, dp = [0, 0, 0, 0]):
        '''
        Displays 4 characters of the given text. The text is considered to be prefixed and postfixed by spaces
        and the 4 character window is selected by the text pointer pos that determines the character displayed at the
        leftmost digit, e.g. (_: empty):
        showText("AbCdEF") -> AbCd
        showText("AbCdEF", 1) -> bCdE
        showText("AbCdEF", -1) ->_AbC
        showText("AbCdEF", 4) -> EF__
        @param text: the text to display (list, tuple, string or integer)
        @param pos: the start value of the text pointer (character index positioned a leftmost digit)
        @param dp: a list with one to four 1 or 0, if the decimal point is shown or not. For compatibility with
        the 4tronix display, the following mapping is used:
        The first element in list corresponds to dp at second digit from the right, the second element to dp
        at third digit from the right, the third element to dp at leftmost digit, the forth element to the dp at
        rightmost digit.  More than 4 elements are ignored
        @return: True, if successful; False, if the display is not available,
        text or dp has illegal type or one of the characters can't be displayed
        '''
        Py7Seg.debug("showText(" + str(text) + "," + str(pos) + "," + str(dp) + ")")
        if not self._isReady:
            return False
        if not (type(text) == int or type(text) == list or type(text) == tuple or type(text) == str):
            return False
        if not (type(dp) == list or type(dp) == tuple):
            return False
        self._startPos = pos
        self._pos = pos
        dpList = [0] * 4
        for i in range(min(4, len(dp))):
              dpList[i] = dp[i]
        self._decimalPoint = [0] * 4
        self._decimalPoint[0] = dpList[2]
        self._decimalPoint[1] = dpList[1]
        self._decimalPoint[2] = dpList[0]
        self._decimalPoint[3] = dpList[3]
        text = str(text)  # convert digits to chars
        self._text = [' '] * len(text)
        for i in range(len(text)):
            try:
                self._text[i] = Py7Seg.PATTERN[text[i]]
            except:
                self._text[i] = 0  # empty
        data = self._getData(self._pos)
        self.writeData(data)
        return True

    def scrollToLeft(self):
        '''
        Scrolls the current text one step to the left by increasing the text pointer.
        @return: the number of characters hidden, but remaining to be displayed at the right (>=0); -1, if error
        '''
        if not self._isReady:
            return -1
        if self._startPos == -1:  # no text yet
            return -1
        self._pos += 1
        data = self._getData(self._pos)
        self.writeData(data)
        nb = len(self._text) - self._pos
        return max(0, nb)

    def scrollToRight(self):
        '''
        Scrolls the current text one step to the left by decreasing the text pointer.
        @return: the number of characters hidden, but remaining to be displayed at the left (>=0); -1, if error
        '''
        if not self._isReady:
            return -1
        if self._startPos == -1:  # no text yet
            return -1
        self._pos -= 1
        pos = self._pos
        data = self._getData(self._pos)
        self.writeData(data)
        return max(0, self._pos)

    def setToStart(self):
        '''
        Shows the scrollable text at the start position by setting the text pointer to its start value.
        @return: 0, if successful; -1, if error
        '''
        if not self._isReady:
            return -1
        if self._startPos == -1:  # no text yet
            return -1
        self._pos = self._startPos
        data = self._getData(self._pos)
        self.writeData(data)
        return 0

    def showTicker(self, text, count = 1, speed = 2, blocking = False):
        '''
        Shows a ticker text that scroll to the left until the last 4 characters are displayed. The method blocks
        until the ticker thread is successfully started and isTickerAlive() returns True.
        @param text: the text to display, if short than 4 characters, scrolling is disabled
        @param count: the number of repetitions (default: 1). For count = 0, infinite duration,
        may be stopped by calling stopTicker().
        @param speed: the speed number of scrolling operations per sec (default: 2)
        @param blocking: if True, the method blocks until the ticker has finished; otherwise
         it returns immediately (default: False)
        '''
        if not self._isReady:
            return
        self.clear();
        if self._tickerThread != None:
            self.stopTicker()
        if self._blinkerThread != None:
            self.stopBlinker()
        self._tickerThread = TickerThread(self, text, count, speed)
        if blocking:
            while self.isTickerAlive():
                continue

    def stopTicker(self):
        '''
        Stops a running ticker.
        The method blocks until the ticker thread is finished and isTickerAlive() returns False.
        '''
        if not self._isReady:
            return
        if self._tickerThread != None:
            self._tickerThread.stop()
            self._tickerThread = None

    def isTickerAlive(self):
        '''
        @return: True, if the ticker is displaying; otherwise False
        '''
        if not self._isReady:
            return False
        Py7Seg.delay(1)
        if self._tickerThread == None:
            return False
        return self._tickerThread._isAlive

    def showBlinker(self, text, dp = [0, 0, 0, 0], count = 3, speed = 1, blocking = False):
        '''
        Shows a ticker text that scroll to the left until the last 4 characters are displayed. The method blocks
        until the ticker thread is successfully started and isTickerAlive() returns True.
        @param text: the text to display, if short than 4 characters, scrolling is disabled
        @param count: the number of repetitions (default: 2). For count = 0, infinite duration,
        may be stopped by calling stopBlinker().
        @param speed: the speed number of blinking operations per sec (default: 1)
        @param blocking: if True, the method blocks until the blinker has finished; otherwise
         it returns immediately (default: False)
        '''
        if not self._isReady:
            return
        self.clear();
        if self._tickerThread != None:
            self.stopTicker()
        if self._blinkerThread != None:
            self.stopBlinker()
        self._blinkerThread = BlinkerThread(self, text, dp, count, speed)
        if blocking:
            while self.isBlinkerAlive():
                continue

    def stopBlinker(self):
        '''
        Stops a running blinker.
        The method blocks until the blinker thread is finished and isBlinkerAlive() returns False.
        '''
        if not self._isReady:
            return
        if self._blinkerThread != None:
            self._blinkerThread.stop()
            self._blinkerThread = None

    def isBlinkerAlive(self):
        '''
        @return: True, if the blinker is displaying; otherwise False
        '''
        if not self._isReady:
            return False
        Py7Seg.delay(1)
        if self._blinkerThread == None:
            return False
        return self._blinkerThread._isAlive

    def showVersion(self):
        '''
        Displays current version. Format X (three horz bars) + n.nn
        '''
        v = "X" + Py7Seg.VERSION.replace(".", "")
        self.showText(v, pos = 0, dp = [0, 1])

    def isAvailable(self):
        '''
        Check if device is available.
        @return: True, if device can be accessed
        '''
        return self._isReady

# -------------------- private methods ----------------------------
    def _getData(self, pos):
        if pos >= 0:
            data = self._text[pos:pos + 4]
            for i in range(4 - len(data)):
                data.append(0) # spaces
        else:
            if 4 + pos >= 0:
                data = self._text[0:4 + pos]
            else:
                data = []
            data.reverse()
            for i in range(4 - len(data)):
                data.append(0) # spaces
            data.reverse()
        for i in range(4):
            data[i] = data[i] + 128 * self._decimalPoint[i]  # add decimal points
        return data

# ------------------- class TickerThread ----------------------
class TickerThread(Thread):
    def __init__(self, display, text, count, speed):
        Thread.__init__(self)
        self._text = text
        self._display = display
        if speed <= 0:
            speed = 1
        self._period = int(1000.0 / speed)
        self._count = count
        self._isRunning = False
        self._isAlive = True
        self.start()
        while not self._isRunning:
            continue

    def run(self):
        Py7Seg.debug("TickerThread started")
        self._display.showText(self._text)
        nb = 0
        self._isRunning = True
        while self._isRunning:
            startTime = time.time()
            while time.time() - startTime < self._period / 1000.0 and self._isRunning:
                Py7Seg.delay(1)
            if not self._isRunning:
                break
            rc = self._display.scrollToLeft()
            if rc == 4 and self._isRunning:
                startTime = time.time()
                while time.time() - startTime < 2 and self._isRunning:
                    Py7Seg.delay(10)
                if not self._isRunning:
                    break
                nb += 1
                if nb == self._count:
                    break
                self._display.setToStart()
        if self._isRunning: # terminated by number of count
            while time.time() - startTime < 2 and self._isRunning:
                Py7Seg.delay(10)
            self._display.clear()
        Py7Seg.debug("TickerThread terminated")
        self._isAlive = False

    def stop(self):
        self._isRunning = False
        while self._isAlive:  # Wait until thread is finished
            continue
        Py7Seg.debug("Clearing display")
        self._display.clear()


# ------------------- class BlinkerThread ----------------------
class BlinkerThread(Thread):
    def __init__(self, display, text, dp, count, speed):
        Thread.__init__(self)
        self._text = text
        self._dp = dp
        self._display = display
        if speed <= 0:
            speed = 1
        self._period = int(1000.0 / speed)
        self._count = count
        self._isRunning = False
        self._isAlive = True
        self.start()
        while not self._isRunning:
            continue

    def run(self):
        Py7Seg.debug("BlinkerThread started")
        nb = 0
        self._isRunning = True
        while self._isRunning:
            self._display.showText(self._text, dp = self._dp)
            startTime = time.time()
            while time.time() - startTime < self._period / 1000.0 and self._isRunning:
                Py7Seg.delay(1)
            if self._isRunning == False:
                break
            self._display.clear()
            startTime = time.time()
            while time.time() - startTime < self._period / 1000.0 and self._isRunning:
                Py7Seg.delay(1)
            if self._isRunning == False:
                break
            nb += 1
            if nb == self._count:
                self._isRunning = False

        startTime = time.time()
        while time.time() - startTime < 1:
            Py7Seg.delay(1)
        Py7Seg.debug("BlinkerThread terminated")
        self._isAlive = False

    def stop(self):
        self._isRunning = False
        while self._isAlive: # Wait until thread is finished
            continue

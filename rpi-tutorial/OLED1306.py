# OLED1306.py
# Support class for the OLED1306 controller based OLED display
# 128x32 or 128x64 resolution.
# Sits on top of the Adafruit OLED1306 driver class (with thanks to the author)

import SSD1306
import RPi.GPIO as GPIO

import os, time
from threading import Thread
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class OLED1306():
    '''
    Creates a display instances with given OLED display type (128x32 or 128x64, black & white).
    with standard font from font file /usr/share/fonts/truetype/freefont/FreeSans.ttf.
    @param imagePath: the path to the PPM image file used as background (must have size 128x32 or 128x64 resp.)
    @param type: 32 or 64 defining 128x32 or 128x64 bit resolution (default: 64)
    @param inverse: if True, the background is white and the text is black; 
    otherwise the background is black and the text  is white (default)
    '''
    def __init__(self, bkImagePath = None, type = 64, inverse = False):
        if type == 32:
            # 128x32 display with hardware I2C:
            self.disp = SSD1306.SSD1306_128_32(rst = None, gpio = GPIO)
        elif type == 64:
            # 128x64 display with hardware I2C:
            self.disp = SSD1306.SSD1306_128_64(rst = None, gpio = GPIO)
        else:
            print "Device type", type, "not supported"
        self.inverse = inverse
        self.bkImagePath = bkImagePath
        self.type = type    
        self.blinkerThread = None

        # Initialize library
        self.disp.begin()
        
        # Get display width and height
        self.width = self.disp.width
        self.height = self.disp.height

        # Clear display
        self.disp.clear()
        self.disp.display()

        # Create 1-bit image buffer
        self.image = Image.new('1', (self.width, self.height))

        # Load font
#        self.font = ImageFont.load_default()
        self.fontSize = 10
#        self.ttfFileStandard = "/home/pi/Fonts/OpenSans-Light.ttf"
        self.ttfFileStandard = "/home/pi/Fonts/OpenSans-Semibold.ttf"
        self.ttfFile = self.ttfFileStandard
        self.font = ImageFont.truetype(self.ttfFile, 10)

        # Create drawing object
        self.draw = ImageDraw.Draw(self.image)

        # Set full contrast
        self.disp.set_contrast(255)

        # Initialize text buffer
        self.textBuf = {}
        self.cursor = [0, 0]
        self.scroll = False
        
    def dim(self, enable):
        '''
        Enables/disables dimming the display.
        @param enable: if True, the display is slightly dimmed; 
        otherwise it is set to full contrast
        '''
        if enable:
            self.disp.set_contrast(0)
        else:
            self.disp.set_contrast(255)
        
    def setBkImage(self, bkImagePath):
        '''
        Defines a background image to be displayed with next setText() or show().
        '''
        self.bkImagePath = bkImagePath
         
    def setFont(self, ttfFile, fontSize = 10):
        ''' 
        Sets a new font defined by the given TTF font file. 
        @ttfFile: the path to the font file (only TTF fonts supported)
        @fontSize: the font size (default: 10)
        '''
        self.ttfFile = ttfFile
        self.ttfFileStandard = ttfFile
        self.fontSize = fontSize
        self.font = ImageFont.truetype(ttfFile, fontSize)

    def setFontSize(self, fontSize):
        '''
        Sets a new font size of current font.
        @fontSize: the new font size
        '''
        self.font = ImageFont.truetype(self.ttfFile, fontSize)
        self.fontSize = fontSize

    def clear(self):
        '''
        Erases the display and clears the text buffer.
        '''
        if self.inverse:
            self.draw.rectangle((0, 0, self.width, self.height), outline = 0, fill = 255)
        else:
            self.draw.rectangle((0, 0, self.width, self.height), outline = 0, fill = 0)
        self.disp.image(self.image)
        self.disp.display()
        self.textBuf = {}
        self.cursor = [0, 0]
        self.scroll = False
        
    def erase(self):
        '''
        Erases the display without clearing the text buffer.
        '''
        if self.inverse:
            self.draw.rectangle((0, 0, self.width, self.height), outline = 0, fill = 255)
        else:
            self.draw.rectangle((0, 0, self.width, self.height), outline = 0, fill = 0)
        self.disp.image(self.image)
        self.disp.display()
                    
    def setText(self, text, lineNum = 0, fontSize = None, indent = 0):
        '''
        Displays text at given line left adjusted.
        The old text of this line is erased, other text is not modified
        The line distance is defined by the font size (text height + 1).
        If no text is attributed to a line, the line is considered to consist of a single space
        character with the font size of the preceeding line.
        The position of the text cursor is not modified.
        Text separated by \n is considered as a  multiline text. In this case lineNum is the line number of the
        first line.
        @param text: the text to display. If emtpy, text with a single space character is assumed.
        @param lineNum: the line number where to display the text (default: 0)
        @param fontSize: the size of the font (default: None, set to current font size)
        @indent: the line indent in pixels (default: 0)
        '''
        if "\n" not in text:
            self._setLine(text, lineNum, fontSize, indent)
        else:
            lines = text.split("\n")
            nb = lineNum
            for line in lines:
                self._setLine(line, nb, fontSize, indent)
                nb += 1
    
    def _setLine(self, text, lineNum, fontSize, indent):
        if text == "":
            text = " "
        if fontSize == None:
            fontSize = self.fontSize
        self.textBuf[lineNum] = (text, fontSize, indent)
        self.repaint()
        
    def getFontSize(self):
        '''
        Returns the current font size.
        @return: the font size
        '''
        return self.fontSize
    
    def getLineHeight(self):
        '''
        Returns the height of one line.
        @return: line spacing in pixels
        '''
        charWidthDummy, charHeight = self.draw.textsize('I', font = self.font)
        return charHeight

    def repaint(self):
        '''
        Repaints the screen (background image and text buffer).
        '''
        maxNum = max(self.textBuf.keys())
        # Clear display
        if self.inverse:
            self.draw.rectangle((0, 0, self.width, self.height), outline = 0, fill = 255) # White
        else:
            self.draw.rectangle((0, 0, self.width, self.height), outline = 0, fill = 0) # Black
        # Insert background image
        if self.bkImagePath != None:
            picture = Image.open(self.bkImagePath).convert('1')
            self.image.paste(picture)
        y = 0
        lastFontSize = 0
        for lineNb in range(maxNum + 1):
            try:
                text = self.textBuf[lineNb][0]
                fontSize = self.textBuf[lineNb][1]
                x = self.textBuf[lineNb][2]  # tab
            except:
                text = " "
                fontSize = 10
                x = 0
            self.font = ImageFont.truetype(self.ttfFile, fontSize)
            charWidthDummy, charHeight = self.draw.textsize('A', font = self.font)
            for c in text:
                charWidth, charHeightDummy = self.draw.textsize(c, font = self.font)
                if self.inverse:
                    self.draw.text((x, y), c, font = self.font, fill = 0)  # Black
                else:
                    self.draw.text((x, y), c, font = self.font, fill = 255) # White
                x += charWidth
            y += charHeight
            
        # Renders the current image buffer.
        self.disp.image(self.image)
        self.disp.display()

    def showImage(self, imagePath):  
        '''
        Shows the image (1 pixel monochrome) with given filename (must have size 128x32 for display type 32 
        or 128x64 for display type 64).
        @param imagePath: the path to the PPM image file
        '''
        picture = Image.open(imagePath).convert('1')
        self.disp.image(picture)
        self.disp.display()
        
    def println(self, text):
        '''
        Appends text at current cursor position and scrolls, if necessary. 
        Sets the cursor at the beginning of next line.
        @param text: the text to display
        '''
        charWidthDummy, charHeight = self.draw.textsize('I', font = self.font)
        nbLines = int(self.type / (charHeight))
    
        if not self.scroll:
            self.setText(text, self.cursor[1])
            self.cursor[1] += 1
            if self.cursor[1] == nbLines:
                self.scroll = True
        else:
            for i in range(nbLines - 1):
                self.textBuf[i] = self.textBuf[i + 1]
            self.setText(text, nbLines - 1)    
        
    def setNumberOfLines(self, nbLines):
        '''
        Sets the current font size to a maximum to show the given number of lines.
        @param: the number of lines to display
        '''
        fontSize = int(self.type / nbLines) + 1
        self.setFontSize(fontSize)
        
    def setInverse(self, inverse):
        '''
        @param inverse: if True, the background is white and the text is black; 
        otherwise the background is black and the text  is white (default)
        '''
        self.inverse = inverse
        self.repaint()
        
    def setBlinking(self, count = 3, offTime = 1, onTime = 1, blocking = False):
        '''
        Blicks the entire screen for given number of times (off-on periods). 
        @param count: the number of blinking (default: 3)
        @param offTime: the time the display is erased (in s)
        @param onTime: the time the display is shown (in s)
        @param blocking: if True, the function blocks until the blinking is finished; otherwise
        it returns immediately
        '''
        if self.blinkerThread != None:
            self.stopBlinker()
        self.blinkerThread = BlinkerThread(self, count, offTime, onTime)
        if blocking:
            while self.isBlinkerAlive():
                continue
                             
    def stopBlinker(self):
        '''
        Stops a running blinker.
        The method blocks until the blinker thread is finished and isBlinkerAlive() returns False.
        '''
        if self.blinkerThread != None:
            self.blinkerThread.stop()
            self.blinkerThread = None

    def isBlinkerAlive(self):
        '''
        @return: True, if the blinker is displaying; otherwise False
        '''
        time.sleep(0.001)
        if self.blinkerThread == None:
            return False
        return self.blinkerThread.isAlive
    
                               
# ------------------- class BlinkerThread ----------------------
class BlinkerThread(Thread):
    def __init__(self, display, count, offTime, onTime):
        Thread.__init__(self)
        self.display = display
        self.offTime = offTime
        self.onTime = onTime
        self.count = count
        self.isRunning = False
        self.isAlive = True
        self.start()
        while not self.isRunning:
            continue

    def run(self):
        nb = 0
        self.isRunning = True
        while self.isRunning:
            self.display.erase()
            startTime = time.time()
            while time.time() - startTime < self.offTime and self.isRunning:
                time.sleep(0.001)
            if not self.isRunning:
                break
            nb += 1
            self.display.repaint()
            startTime = time.time()
            while time.time() - startTime < self.onTime and self.isRunning:
                time.sleep(0.001)
            if not self.isRunning:
                break
            if nb == self.count:
                self.isRunning = False
        self.isAlive = False

    def stop(self):
        self.isRunning = False
        while self.isAlive: # Wait until thread is finished
            continue
                                                                                         

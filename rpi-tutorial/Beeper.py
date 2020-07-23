# Beeper.py

from threading import Thread
import RPi.GPIO as GPIO
import time

debug = False

class Beeper():
    def __init__(self, pin):
        if debug:
            print "Creating Beeper"
        self._pin = pin
        self._beeperThread = None
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    
    def start(self, onTime, offTime, count = 0, blocking = False):
        '''
        Starts beeping. The beeping period is offTime + onTime. 
        May be stopped by calling stopBlinker(). If blocking is False, the
        function returns immediately while the blinking goes on. The blinking is stopped by setColor().
        @param onTime: the time in ms in on state
        @param offTime: the time in ms in off state
        @param count: total number of on states; 0 for endlessly (default)
        @param blocking: if True, the method blocks until the beeper has finished; otherwise
         it returns immediately (default: False)
        '''
        if debug:
            print "Starting beeper with params", onTime, offTime, count, blocking
        if self._beeperThread != None:
            self.stop()
        self._beeperThread = BeeperThread(self, onTime, offTime, count)
        if blocking:
            while self.isBeeping():
                continue

    def setOffTime(self, offTime):
        if self._beeperThread != None:
            self._beeperThread._offTime = offTime

    def setOnTime(self, onTime):
        if self._beeperThread != None:
            self._beeperThread._onTime = onTime

    def setOnOffTime(self, onTime, offTime):
        if self._beeperThread != None:
            self._beeperThread._onTime = onTime
            self._beeperThread._offTime = offTime
       
    def stop(self):
        '''
        Stops beeping.
        '''
        if self._beeperThread != None:
            self._beeperThread.stop()

    def isBeeping(self):
        '''
        @return: True, if the beeper is active; otherwise False
        '''
        time.sleep(0.001)
        return self._beeperThread != None
    
    def cleanup(self):
        GPIO.cleanup()

# ------------------- class BeeperThread ----------------------
class BeeperThread(Thread):
    def __init__(self, beeper, onTime, offTime, count):
        Thread.__init__(self)
        self._beeper = beeper
        self._onTime = onTime
        self._offTime = offTime
        self._count = count
        self._isAlive = True
        self.start()

    def run(self):
        if debug:
            print("Beeper thread started")
        nb = 0
        self._isRunning = True
        while self._isRunning:
            if self._onTime <= 0:
                GPIO.output(self._beeper._pin, GPIO.LOW)
                time.sleep(0.01)
            else:
                GPIO.output(self._beeper._pin, GPIO.HIGH)
                startTime = time.time()
                while time.time() - startTime < self._onTime and self._isRunning:
                    time.sleep(0.001)
                if not self._isRunning:
                    break
    
                GPIO.output(self._beeper._pin, GPIO.LOW)
                startTime = time.time()
                while time.time() - startTime < self._offTime and self._isRunning:
                    time.sleep(0.001)
            if not self._isRunning:
                break

            nb += 1
            if nb == self._count:
                self._isRunning = False
        GPIO.output(self._beeper._pin, GPIO.LOW)
        self._beeper._beeperThread = None
        self._isAlive = False
        if debug:
            print("Beeper thread finished")

    def stop(self):
        self._isRunning = False
        while self._isAlive: # Wait until thread is finished
            continue

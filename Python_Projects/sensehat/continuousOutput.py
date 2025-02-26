import logging
import logging.handlers
import time
import sys
from sense_hat import SenseHat
my_logger = logging.getLogger('my_test_logger');
rfh = logging.handlers.RotatingFileHandler(filename = 'log.txt',\
                                          maxBytes = 1024,\
                                           backupCount = 2)
my_logger.setLevel (logging.INFO)

formatter = logging.Formatter ('%(asctime)s - %(message)s')
rfh.setFormatter (formatter)
my_logger.addHandler(rfh)
my_logger.info ('test')
sense = SenseHat()
try:
    while True:
        my_logger.info ('test')
        #user_input = str(raw_input('inval'))
        print ('Hit cntrl-c to stop the program')
        
        orientation_rad = sense.get_orientation_radians()
        #print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_rad))
        my_logger.info('p: {pitch}, r: {roll}, y: {yaw}'.format(**orientation_rad))
        
##        orientation = sense.get_orientation_degrees()
##        print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
##
##        north = sense.get_compass()
##        print("North: %s" % north)
##
##        gyro_only = sense.get_gyroscope()
##        print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))
##
##        raw = sense.get_gyroscope_raw()
##        print("x: {x}, y: {y}, z: {z}".format(**raw))
##
##        accel_only = sense.get_accelerometer()
##        print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))
##
##        raw = sense.get_accelerometer_raw()
##        print("x: {x}, y: {y}, z: {z}".format(**raw))
##
##        humidity = sense.get_humidity()
##        print("Humidity: %s %%rH" % humidity)
##
##        temp = sense.get_temperature()
##        print("Temperature: %s C" % temp)
##
##        pressure = sense.get_pressure()
##        print("Pressure: %s Millibars" % pressure)
##
##        my_logger.info(user_input)
        time.sleep(0.1)
    
    
except KeyboardInterrupt:
    #my_logger.close()
    sys.exit(0)

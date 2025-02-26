#Sensor Tests
#from https://pythonhosted.org/sense-hat/api
from sense_hat import SenseHat

sense = SenseHat()
orientation_rad = sense.get_orientation_radians()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_rad))

orientation = sense.get_orientation_degrees()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

north = sense.get_compass()
print("North: %s" % north)

gyro_only = sense.get_gyroscope()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))

raw = sense.get_gyroscope_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))

accel_only = sense.get_accelerometer()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))

raw = sense.get_accelerometer_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))

humidity = sense.get_humidity()
print("Humidity: %s %%rH" % humidity)

temp = sense.get_temperature()
print("Temperature: %s C" % temp)

pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)

import RPi.GPIO as GPIO
import time, math
#https://theengineeringmindset.com/capacitor-charge-time-calculation/
#For a 100uF capacitor by experiment I got the following liniear relationship
#With an Rsquared value of .999
#Resistance = 19778 time +280 
R1 = 1000 # Ohms
Voltage_On_Threshold = 1.65 #Voltage that triggers high reading
Voltage_max = 3.3 #Max voltage out of capacitor
Time_Constant_Percentage = 0.632 #Percentage elapsed
#to first time constant reached

GPIO.setmode(GPIO.BCM)

# Pin a charges the capacitor through a fixed 1k resistor and the thermistor in series
# pin b discharges the capacitor through a fixed 1k resistor 
a_pin = 18
b_pin = 24

# empty the capacitor ready to start filling it up
def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.1)

# return the time taken (uS) for the voltage on the capacitor to count as a digital input HIGH
# than means around 1.65V
def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    GPIO.output(a_pin, True)
    t1 = time.time()
    while not GPIO.input(b_pin):
        pass
    t2 = time.time()
    return (t2 - t1) 

# Take an analog reading as the time taken to charge after first discharging the capacitor
def analog_read():
    discharge()
    print ("Finished Discharge")
    t = charge_time()
    print ("Charge Time:" + str(t) )
    discharge()
    return t

# Convert the time taken to charge the cpacitor into a value of resistance
# To reduce errors, do it 100 times and take the average.
def read_resistance():
    n = 10
    total = 0;
    for i in range(1, n):
        total = total + analog_read()
    t = total / float(n)
    #T = t * Time_Constant_Percentage  * Voltage_max / Voltage_On_Threshold
    #r = (T / C) - R1
    r = (19778*t +280)-R1
    return r
try:
    while True:
        print("Resistor = " + str(read_resistance()))
        time.sleep(2)
finally:
    GPIO.cleanup()


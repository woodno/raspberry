from machine import PWM, Pin, UART
import time # Import time library which lets us use the sleep command
import gps_parser #put gps_parser in the python path usually below lib
led = Pin("LED", Pin.OUT) # Set up the onboard LED (can replace "LED" with a pin GPIO number)



#This program runs a self test on the car on startup

#Function defs and constant defs that use no GPIO Function

# this varaible is used to help calculate the required input from a duty cycle percentage
# the value for the duty cycle is held as 2 bytes of data.
# 2^16 = 65536. 
max = 65535

def getPWMFromPercentage(percentage):
    PWM_value = int(percentage/100 * max)
    print ("My PWM_value is", PWM_value)
    return PWM_value



#Test1 LED blinks for 5 times at 1 second intivals

i = 0

try:
    while i < 5:  
        led.value(1)  # Turn the LED ON
        time.sleep(1) # Go to sleep for 2 seconds
            
            
        led.value(0)  # Turn the LED OFF
        time.sleep(1) # Go to sleep for 2 seconds
        i = i + 1
        print ("im here after run " + str(i) )
    #Test2 GPS test
    #Tries 300 times each 1 second to get a GPS fix
    #If successful it lights up the onboard led for 10 seconds 
    uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

    # Create a GPS reader object
    gps = gps_parser.GPSReader(uart)

    i = 0
    while i < 300:
        # Get the GPS data, this will also try and read any new information form the GPS
        gps_data = gps.get_data()
        
        # Print the GPS data
        print(gps_data.has_fix, gps_data.latitude, gps_data.longitude)
        if (gps_data.has_fix):
            led.value(1)  # Turn the LED ON
            time.sleep(10)
            break
        # Small delay
        time.sleep(0.5)
        
        i = i + 1
finally:
	led.value(0)
	led = Pin("LED", Pin.IN) 
	print ("I've cleaned up after " + str(i) + " runs")

#Test2 Drive motor test.
pwm_enable_drive_motor = PWM(Pin(3))
# this sets up the frequency that the pin is turned off and on (it is not duty cycle)
# all constants should be set at the beginning of the program
# later on we will learn how to do this.
pwm_enable_drive_motor.freq(1000)
pwm_enable_servo = PWM(Pin(10))
pwm_enable_servo.freq(1150)

#The following pin out is in relation
#to the L293D motor driver
#this setup facilitates one motor running in forward or reverse mode
# Using more pins the driver can run another motor forward or reverse.
#This is the pin out starting from the top left (Notch is the top)
#Pin 1 enable = GPIO pin 3 (PWM pin)
#Pin 2 = GPIO pin 4
#Pin 3 OUT 1 = motor lead 1
#Pin 4 GND = GND Pi
#Pin 5 If using an external power source connect to the ground of that.
#Pin 12, 13 are also GND that can be used to ground the external power supply or Pico
#Pin 4,5,12 and 13 are internally connected so can be used for any ground. 
#Pin 6 = motor lead 2
#Pin 7 = = GPIO 5
#Pin 8 (Vs) =  9V on power supply (Supplies power to the motor)
#Pin 16 (Vss) = 3.3 V Powers the board logic 

#IC pins are numbered 1 and up anticlockwise.
# pin 16 is top right.


input1_pin = Pin(4, Pin.OUT)
input2_pin = Pin(5, Pin.OUT)
c1 = Pin(6, Pin.OUT)
c2 = Pin(7, Pin.OUT)




percentagePWM = 100
hasForwardDirection = True

try:
    #Test2 Servo Motor test.
    print ("got here")
    pwm_enable_servo.duty_u16(getPWMFromPercentage(100))
    c1.value(1)
    c2.value(0)
    time.sleep(2)
    c1.value(0)
    c2.value(0)
    time.sleep(2)
    c1.value(0)
    c2.value(1)
    time.sleep(2)
    #Test3 Drive Motor Test
    i = 0
    while i < 2:
        if percentagePWM < 0:
            percentagePWM = 100
            hasForwardDirection = not hasForwardDirection
            i = i + 1
        pwm_enable_drive_motor.duty_u16(getPWMFromPercentage(percentagePWM))
        print ("My motor is running at ", percentagePWM , "%")
        if (hasForwardDirection):
            print ("Forwards")
            input1_pin.value(1)
            input2_pin.value(0)
        else:
            print ("Backwards")
            input1_pin.value(0)
            input2_pin.value(1)
        time.sleep(2)
        percentagePWM = percentagePWM - 10
        
    
    

finally:
    pwm_enable_drive_motor.deinit()
    inputpwm_pin = Pin(3, Pin.IN)
    input1_pin = Pin(4, Pin.IN)
    input2_pin = Pin(5, Pin.IN)
    pwm_enable_servo.deinit()
    inputpwm_pin = Pin(10, Pin.IN)
    input1_pin = Pin(6, Pin.IN)
    input2_pin = Pin(7, Pin.IN)
    print ("I've cleaned up")




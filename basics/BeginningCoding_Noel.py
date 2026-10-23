#File_Name BeginningCoding_Noel.py
#Program Structure
#Imports
import time
#Constants
PI = 3.14159
#Global Variables
radius = 25
#Functions
def circum(radius):
    circum = 2 * PI * radius
    print("Radius in function = ",radius)
    return circum
#Main Program
c = circum (radius)
print ("Circum =",c)
print ("Circum ="+str(c))

c = circum(100)
print("Radius in main = ",radius)
print ("Circum ="+str(c))
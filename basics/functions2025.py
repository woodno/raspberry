#Work out the area of circles from 1 to 100 radius in increments of 1
def area (radius):
    #The following line is to teach about the scope of a variable
    #pi = 3.14 
    return pi * radius * radius

def circum (radius):
    return 2 * pi * radius

pi = 3.14
for i in range (101):
    print ("The area of a circle with radius " + str(i) + " is "  + str(area (i)))
    print ("The circumfrance of a circle with radius " + str(i) + " is "  + str(circum (i)))
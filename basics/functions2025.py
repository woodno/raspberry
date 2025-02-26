#Work out the area of circles from 1 to 100 radius in increments of 1
pi = 3.14
def area (radius):
    #The following line is to teach about the scope of a variable
    #pi = 3.14
    areaans = pi * radius  ** 2
    return areaans

def circum (radius):
    return 2 * pi * radius


for i in range (101):
    print ("The area of a circle with radius " + str(i) + " is "  + str(area (i)))
    print ("The circumfrance of a circle with radius " + str(i) + " is "  + str(circum (i)))
#Work out the area of circles from 1 to 100 radius in increments of 1
pi = 3.14
def area (radius):
    #The following line is to teach about the scope of a variable
    global pi
    pi = 16
    areaans = pi * radius  ** 2
    return areaans

def circum (radius):
    return 2 * pi * radius

cir = circum(45)
print (cir)
areaofradius10 =area(10)
print (areaofradius10)
print(7%2)


# for i in range (101):
#     print ("The area of a circle with radius "
#            + str(i) + " is "  + str(area (i)))
#     print ("The circumfrance of a circle with radius "
#            + str(i) + " is "  + str(circum (i)))
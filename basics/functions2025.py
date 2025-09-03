pi = 3.14
def area (radius):
    #The following line is to teach about the scope of a variable
    #global pi
    #pi = 16
    areaans = pi * radius  ** 2
    return areaans

def circum (radius):
    return 2 * pi * radius

cir = circum(45)
print (cir)
areaofradius10 =area(10)
print (areaofradius10)



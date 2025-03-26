import math
#Write an area function

def getAreaFromRadius(radius):
    area = math.pi * radius * radius
    return area

#Write a circum function

def getCircumFromRadius(radius):
    circum = 2 * math.pi * radius
    return circum
##Take in an input
# age = input ("What is your age?")
# print ("Your age is " + age)
# radius = input ("What radius do you want the area of?")
# print (radius)
# radf = float(radius)
# print (getAreaFromRadius(radf))
##Make it an float
##Find the area using it

#Split it in two.

#Testing area
# print (math.pi)
# #print out the area of a circle of radius 10
# area = getAreaFromRadius(10)
# #print (getAreaFromRadius(10))
# print (area)
# 
# #print out the circumfrance of a circle of radius 10
# print (getCircumFromRadius(10))

inputComplex = input ("Enter a sentance in the format [a,c],[number],[unit]")
inputList = inputComplex.split(",")
print (inputList)
radiusAsNum = float(inputList[1])
if inputList[0] == 'a':
    print ("you want the area")
    myArea = getAreaFromRadius(radiusAsNum)
    print ("The area for your radius is " + str (myArea) + inputList[2] + "squared") 
else:
    print ("you want the circumfrance")
    myCircum = getCircumFromRadius(radiusAsNum)
    print ("The circum for your radius is " + str (myCircum) + inputList[2]) 
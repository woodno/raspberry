 
# x  = 10
# y = 3 
# if x > 10:
#   print ("Bigger than 10")
#   y = 15 #changed
# if x < 10:
#   print ("Smaller than 10")
#   y = 7
# if x == 10:
#   print ("It is 10")
#   y = 16
#  
# print ("y = " , y)

# if x > 100 and if y is odd divide them

#TODO if x > 100 or y is odd floor divide x by y (//)

#TODO if x > 100 and y not = 10 (do two ways using comparrison and not operator)
#TODO then take x to the power of y (**)
#TODO if x > 100 xor y is odd modulo x by y
#False condition
x = 110
y = 3
#False
x = 90
y = 7
#true
x = 110
y = 7
#true
x =90
y= 4


if x > 100:
    if y < 5:
        print ("false")
    else:
        z = x % y
        print ("x modulo y = " , z)
else:
    if y < 5:
        z = x % y
        print ("x modulo y = " , z)
    else:
        print ("false")
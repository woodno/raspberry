while(True):
    
    y = input ("Input a number ")
    #if  "x" in y:
    if not y.isnumeric():
        break
    x = int (y)
    
    
    #x = 4
    if x > 10:
        print ("Bigger than 10")
    elif x < 10:
        print ("Smaller than 10")
    else:
        print ("It is 10")
print ("goodbye")
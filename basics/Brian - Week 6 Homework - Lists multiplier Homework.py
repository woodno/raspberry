
#******** Week 6 Homework *********


# Recreate the original full list
sqnums = []

for i in range (1,21):
    sqnums.append(i ** 2)


#Get muliplier from user and check it is an integer
yourinput = False
while yourinput == (False):
    try:
        multi = int(input("What number would you like to multiply each number in the list by ? "))    
    except ValueError:
        print("Only enter numbers please")
    else:
        yourinput = (True)  



#Iterate through the list and multiply each member by the multiplier input by the user
for i in range (1,len(sqnums)+1):
    newnum = i*multi
    sqnums.append(newnum)

print()
print("The new interated original list looks like this:")
print(sqnums)

print()


#Get a position in the list from user and check it is an integer
arraylength=len(sqnums)

yourpos = False
while yourpos == (False):
    try:
        posnum = int(input("Enter a position number (Index) in the new list between 1 and 40: "))
    except ValueError:
        print("Only enter numbers please")
        continue


    if posnum >arraylength: 
        print ("Number must be between 1 -",arraylength)
    
    elif posnum <1:    
        print ("Number must be greater than 0)")
    
    else:
        yourpos = (True)  



#Print out a statement saying whether a list item is smaller than 2500, bigger than 2500 or 2500 using if, elif and else
#Using item at index position input by the user
    
posnum=posnum-1
print()
print("Position ",posnum+1," in the index is number ",sqnums[posnum])
print()
if sqnums[posnum] <2500:
    print(sqnums[posnum], "is less than 2500")
elif sqnums[posnum] >2500:
    print(sqnums[posnum], "is greater than 2500")
else:
    print(sqnums[posnum], "equals 2500")
  
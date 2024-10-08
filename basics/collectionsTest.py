cars = ["Toyota", "Ford", "Tesla"]
print (cars [1])
cars[1] = "Volvo"
print (cars [1])
x = cars[2]
print (x)
#print (cars[3])
cars.append("Audi")
print (cars[3])
print (len(cars))
x = range(len(cars))
for n in x:
  print(str(n)+" "+ cars[n])
  
for x in cars:
  print(x)
cars.pop(1)
x = range(len(cars))
for n in x:
  print(str(n)+" "+ cars[n])
#for x in cars:
#  print(x)


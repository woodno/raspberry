#Scoping of Variables
x=5
print(x)

def scope ():
    x=3
    print ("x in scope function = " + str (x))
def scope2 ():
    global x
    x=3
    print ("x in scope function = " + str (x))
scope()
print ("x out of scope =" + str(x))
scope2()
print ("x out of scope2 function =" + str(x))

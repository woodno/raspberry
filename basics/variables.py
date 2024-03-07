#Week 4 variables work.


x = "awesome"

#Example 1 Scope of a non-global/global variable
def myfunc():
    x = "great"
    print("Python is " + x)
    
def myfunc2():
    global x
    x = "great"
    print("Python is " + x)
    
myfunc()
print("Python is " + x)
myfunc2()
print("Python is " + x)


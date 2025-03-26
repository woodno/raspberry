#Classes and Objects
#Examples from...
#https://www.w3schools.com/python/python_classes.asp
#https://www.w3schools.com/python/python_inheritance.asp
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)
p1.x = 6
print(p1.x)

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname) 


#Use the Person class to create an object, and then execute the printname method:

z = Person("John", "Doe")
z.lastname = "Jones"
z.printname()

#Inheritance
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
#Note printname works even though 
x.printname()
x.welcome()

#Whats it used for.
#To store data in Lists and do calculations
#Eg You want to store the data you get from multiple inputs and do a calculation
#Hwk
#Create an object called BankLoan
#Its members are principal, rate and time
#Write a printStatement method to calculate and print the interest and return amout  using simple interest
#Test your work by creating a BankLoan object and calling the printStatement method
#Extension create a list of 4 BankLoan objects and call the printStatement method for each.

class BankLoan:
    def __init__(self,principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time
    def interestPayment(self):
        return self.principal * self.rate / 100 * self.time
        
    def printStatement(self):
        print ("Your interest is " + str(self.interestPayment()))
        print ("Your Total Payment is " + str(self.principal + self.interestPayment()))
    
x = BankLoan(1000,10,5)
x.printStatement()
y = BankLoan (5000, 2, 7)
z = BankLoan (2000,6, 25)
a = BankLoan (600000,5.7, 25)
bankLoanList = [x,y,z,a]
for i in range(len(bankLoanList)):
    bankLoanList[i].printStatement()
    




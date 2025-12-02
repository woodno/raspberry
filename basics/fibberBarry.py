#Purpose: Write a program to generate the Fibonacci series
#Author : Barry Mahoney
#Class : RasPi
#File : file_name.py
#Descrip: This program calculates and prints the Fibonacci Series
# stopping at the first number after 100,000.

# Add Libraries

# Add Constants
Fib_num1 = 1
Fib_num2 = 1
Fib_num3 = 0
stop_num = 1042

# Add Declaired functions

# Add Main program
print (Fib_num1)
print (Fib_num2)

while (Fib_num3 < stop_num):
    Fib_num3 = Fib_num1 + Fib_num2
    print (Fib_num3)
    Fib_num1 = Fib_num2
    Fib_num2 = Fib_num3
#     if Fib_num3 > stop_num:
#         break

# Add any cleanup or closure
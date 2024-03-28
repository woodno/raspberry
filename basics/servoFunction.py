#Creating a function to output pwm values for a servo control
#This function outputs pwm values for degrees entered for
#a servo motor
#Argument degree is the degree to turn the motor
#Expected values between 0 - 180
#Return is the pwm value to set
#Exceptions....
def pwmOutputFromDegree(degree):
    y = 2.5/90 * degree + 5
    return y

# print (pwmOutputFromDegree(45))
# print (pwmOutputFromDegree(twenty))

y = float(input ("Enter a degree "))
print(pwmOutputFromDegree(y))
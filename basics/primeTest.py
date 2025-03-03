from datetime import date, datetime, timedelta
#from time import sleep
start_time = datetime.now()
print(start_time)
#end_time = start_time + timedelta(hours=1)
#end_time = start_time + timedelta(minutes=1)
end_time = start_time + timedelta(seconds=1)
counter = 1
def isPrime(number):
    #isPrimeNo = True This is Barry's code (BC)
    for i  in range (2, int(number/2) +1):
        if ( number % i == 0 ):
            #isPrimeNo = False (BC)
            #break (BC)
            return False
    #return isPrimeNo (BC)
    return True    
while datetime.now() < end_time:
    counter = counter + 1
    if (isPrime(counter)):
        print (str(counter) + " is prime")
        
print(datetime.now())
    
# 2115427 is prime
# 2115431 is prime
# 2115433 is prime
# 2115437 is prime
def isPrime(number):
    #isPrimeNo = True
    for i  in range (2, int(number/2) +1):
        if ( number % i == 0 ):
            #isPrimeNo = False
            #break
            return False
        
    return True

print (isPrime (8))
print (isPrime (11))
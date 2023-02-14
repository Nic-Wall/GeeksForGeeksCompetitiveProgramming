#My Attempt
def myAttempt(primeNumber):
    for i in range(2,primeNumber):
        if primeNumber % i == 0:
            return False
    return True
"""
Knowing a prime number is only divisible by itself and one I simply checked the modulus of the entered number with every incremental step of one until I reached primeNumber - 1.
If the number is evenly divisible by one of the indexes in the range 2 - primeNumber it is not a prime number and a false is returned. If the loop completes without ever
having a modulus of 0 the number is a prime number and a True is returned.
"""

#Geeks for Geeks
def GfG(primeNumber):
    if primeNumber <= 1:
        return False
    for i in range(2,primeNumber):
        if primeNumber % i == 0:
            return False
    return True
"""
Almost identical to my own, barring their case checking for any number <= 1. Since 1,0, and anything negative cannot be prime this use case is neccessary.
In my own example if, for example, a -2 is entered my function will return true, where as GfG's function will not. It will not even perform a calculation, just a logical check.
"""

#Main
def main():
    
    
    arrOFunctions = [myAttempt,GfG]
    for function in arrOFunctions:
        primeNumber = 67
        print(f"{function.__name__}: " + str(function(primeNumber)))

main()
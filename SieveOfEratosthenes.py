#My Attempt
def myAttempt(limit):
    limitArray = [True for i in range(2,limit)]
    listOfPrimes = []
    for i in range(2,limit):
        if(limitArray[i-2]):
            for j in range(i*i,limit,i):
                limitArray[j-2] = False
    for i in range(0,len(limitArray)):
        if(limitArray[i]):
            listOfPrimes.append(i+2)
    return listOfPrimes
"""
My first thought was to analyze each integer until a prime was found, then add it to an array, until all number were reached. Such as...
    listOfPrimes = []
    for i in range(2, limit):
        isPrime = True
        if i <= 1:
            pass
        else:
            for j in range(2, i):
                if i % j == 0:
                    isPrime = False
            if isPrime:
                listOfPrimes.append(i)
But for a larger number limit the multiple loops would considerably slow down the program, and I know if a number is prime all subsequent multipliers are NOT.
    Ex. If 3 is prime 6,9,12,15,18,21,etc. would not be.
To solve this I ran an array of booleans parallel to the range(2, limit). If a prime was found all subsequent multipliers in range prime*prime to the limit by step of prime
were not prime and changed to False in the boolean array.
Then using the boolean array I could check only those numbers which had not been removed from the list due to being a mutliple of a previous number.
While faster than my first attempt (due to the above reason) it still contained a loop within a loop which I'm skeptical could be beat
"""

#Geeks for Geeks
def GfG(limit):
    Primes = [0] * limit
    Primes[0] = 1
    i = 3
    while(i*i <= limit):
        if(Primes[i//2] == 0):
            for j in range(3 * i, limit+1,2*i):
                Primes[j//2] = 1
        i += 2
    listOfPrimes = []
    for i in range(1,limit+1):
        if(i == 2):
            listOfPrimes.append(i)
        elif(i % 2 == 1 and Primes[i // 2] == 0):
            listOfPrimes.append(i)

    return listOfPrimes
"""
GfG's approach is significantly faster because they stop at i squared rather than continuing through to the limit as I did. Meaning it makes half the calculations.
"""

#Main
def main():
    limit = 25
    arrOFunctions = [myAttempt,GfG]
    for function in arrOFunctions:
        print(f"{function.__name__}: " + str(function(limit)))

main()
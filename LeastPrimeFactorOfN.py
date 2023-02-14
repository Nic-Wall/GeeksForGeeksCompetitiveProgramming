#My Attempt
def myAttempt(maxR):
    Nums = [i for i in range(3,maxR+1,2)] #Creating array of only odd number
    Sieve = [True for i in range(3, maxR+1, 2)]  #Creating a parallel array

    for i in range(0,len(Sieve)): #Indexes through a range, length of the sieve
        if(Sieve[i]):           #If the given number is susected of being prime it...
            for j in range(i+1,len(Sieve)):     #Starts a new index of one greater than the current i index
                if (Sieve[j] == True) & (Nums[j] % Nums[i] == 0):   #If the j index is True (meaning it hasn't been evaluated and eliminated previously) and it is divisible by...
                    Sieve[j] = False                                    #Num[i], it's marked False. After being marked False it is not referenced again
    
    primes = []
    for i in range(0,len(Sieve)):   #Finds the prime numbers (those left marked True in the sieve) are added to a list just for primes
        if(Sieve[i]):
            primes.append(Nums[i])

    for i in range(2, maxR+1):  #Determines if the number is even or odd
        if i % 2 == 0:          #If even the lowest prime will always be 2
            LPN = 2
        else:                   #If not the numbered is divided by...
            for j in primes:    #the list of primes
                if i % j == 0:  #and as soon as the first divisible prime is found it leaves the loop
                    LPN = j
                    break
        print(f"Least Prime Factor of {i}: {LPN}")

    return 0
"""
I can use the sieve of Eratosthenes to find the primes up to the max range, then solve i % prime == 0 and the first occurance is the least prime factor.
Any even number will always have the lowest prime of 2, which means I don't have to solve against every prime, I can just put in 2.
    Nums = [i for i in range(2,maxR)]     #Numerical represntation
    Sieve = [True for i in range(2,maxR)]   #Boolean representation
    for i in range(2,maxR):
        if(Sieve[i-2]):     #Checking to see if it is marked primes
            for j in range(i*i,maxR,i):     #Incrementing by the prime to the max number
                Sieve[j-2] = False          #Setting each step to False as it has a mutliplier of a prime number

    Primes = []     #Creating an array to hold the prime numbers
    for i in range(0,maxR-2):
        if(Sieve[i]):   #If the index is prime...
            Primes.append(Nums[i])  #Append it to the Primes array

    for i in range(0,maxR-1): #Starting an indexer for the arrays, which will flow from 2 to the max range
        if((i+2) % 2 == 0): #If the number is divisible by 2 it's lowest prime is 2
            prime = 2
        else:               #If not...
            for j in Primes:    #For each previously discovered prime number...
                if (i+2) % j == 0:  #Take the number from the range and divide it by the prime, if it's evenly divisible that is it's least prime factor
                    prime = j
                    break
        print(f"Least Prime Factor of {i+2}: {prime}")

In fact, I don't even need to compute the arary space for even numbers. Which I've done above. It still uses two loops but each array is only half the size!
This was a fun challenge and gave me an opportunity to work on the Sieve of Eratosthenes again, I'm sure GfG did it without loops inside of loops as I did, but since
I couldn't remember the solution from the first time I did the sieve I used what I did know and tried to make it as efficient as possible (so as to not cheat).
"""

#Geeks for Geeks
def GfG(maxR):
    leastPrime = [0] * (maxR + 1)
    leastPrime[1] = 1

    for i in range(2, maxR + 1):
        if(leastPrime[i] == 0):
            leastPrime[i] = i
            for j in range(i * i, maxR + 1, i):
                if(leastPrime[j] == 0):
                    leastPrime[j] = i
    for i in range(1, maxR + 1):
        print(f"Least Prime Factor of {i}: {leastPrime[i]}")
    return 0
"""
GfG's code is considerably faster than my own. But I'm happy with what I created. 
I should also note, I excluded 1 because it is not a prime number, but the GfG example includes it
"""

#Main
def main():
    maxR = 50
    arrOFunctions = [myAttempt,GfG]
    for function in arrOFunctions:
        print(function.__name__)
        function(maxR)
        print()

main()
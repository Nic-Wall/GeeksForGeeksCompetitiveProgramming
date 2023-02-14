import math
#My Attempt
def myAttempt(NatNum):
    factors = []
    HNN = NatNum // 2
    for i in range(1,HNN):
        if NatNum % i == 0:
            factors.append(i)
    factors.append(NatNum)  #Did it here instead of at the HNN declaration to keep them in numerical order
    return factors
"""
My first hought was to divide the number by each increment, steps of 1, until the totals were found. Like so...
factors = []
    for i in range(1,NatNum+1):
        if NatNum % i == 0:
            factors.append(i)
But this isn't necessary as I know from previous GfG examples recursive functions usually provide the best solution.
My next thought was to find the largest factor, then find the largest factor of that, etc. until each are found. The only thing I would need to account for is the divisibility by 2.
Although, it woul still technically loop through all integers because it would (for instance) start at 50, then 49, 48, 47,..., until 25 where it would feed 25 into itself and start
Counting down again this time starting at 25, then 24, 23, 22, 21,etc. In this way it would also pass (not include) 10.
I know finding all the factors between 1 and n/2 would give me factors from both halves of n, so I tried the above...
I know the next best solution would be to take the factors of the factors incrementing in steps based on the factors but how I'm not sure how...
"""

#Geeks for Geeks
def GfG(NatNum):
    i = 1
    factors = []
    while i <= math.sqrt(NatNum):
        if(NatNum % i == i):
            factors.append(i)
        else:
            factors.append(i)
            factors.append(int(NatNum/i))
    return 0
"""
GfG found the solution though
"""

#Main
def main():
    NatNum = 100
    arrOFunctions = [myAttempt,GfG]
    for function in arrOFunctions:
        print(f"{function.__name__}: " + str(function(NatNum)))

main()
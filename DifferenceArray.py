"""
NOTE: I did not finish this one's GfG portion as I don't fully understand what is required. I will probably recreate it on it's on .py file and run it there
Link: https://www.geeksforgeeks.org/difference-array-range-update-query-o1/
"""

#Imports
import random

#My Attempt
def myAttemptUpdate(start,end,x):
    for i in range(start, end + 1):
        myArray[i] += x
    return 0

def myAttemptPrint():
    for i in myArray:
        print(f"{i} ", end="")
    print() #clearing the end=""
    return 0
"""
Since Geeks for Geeks doesn't allow the use of the array as a function parameter I simply created it as a global variable.
Using a loop I added the the requested input into the proper indexes and a second loop (in the print function) to print each index next to one another.
"""

#Geeks for Geeks
def initizalizngArray():
    #Initizalizing the base array
    n = len(baseArray)
    GfGArray = [0 for i in range(0,n+1)]
    GfGArray[0] = baseArray[0]; GfGArray[n]
    for i in range(1, n):
        GfGArray[i] = baseArray[i] - baseArray[i - 1]

def GfGUpdate(start,end,x):   
    GfGArray[start] += x
    GfGArray[end + 1] -= x
    return 0

def GfGPrint():
    for i in range(0, len(baseArray)):
        if(i == 0):
            baseArray[i] = GfGArray[i]
        else:
            baseArray[i] = GfGArray[i] + baseArray[i - 1]
        print(baseArray[i], end="")
        print("")
    return 0
"""
What I must have missed was the request that the difference array be created and displayed in O(1).
I'll have to come back to this one, because I don't quite understand what GfG is requesting
"""

#Main
def main():
    myAttempt = [myAttemptUpdate,myAttemptPrint]
    initizalizngArray()
    GfG = [GfGUpdate, GfGPrint]
    arrOFunctions = [myAttempt,GfG]
    fillerArray = [0,1,10,1,3,20,2,2,30]
    for function in arrOFunctions:
        print(f"\n{function[1].__name__}:")
        for i in range(0,len(fillerArray),3):
            print(f"Update({fillerArray[i]},{fillerArray[i+1]},{fillerArray[i+2]})")
            function[0](fillerArray[i],fillerArray[i+1],fillerArray[i+2])
            function[1]()
        
baseArray = [10, 5, 20, 40]
myArray = GfGArray = baseArray
print("Base Array: ")
for i in baseArray:
    print(f"{i} ", end="")
print() #Clearing the end=""
main()
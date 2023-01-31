import random
#My Attempt
def myAttempt(arr):
    return(sum(arr))
"""
Before using sum I planned to create a running total and itterate through each index, like...
total = 0
for index in arr:
    total += index
return index
But with sum there only exists one line and (for large arrays) the iterations are handle in a much less time consuming way
"""

#Geeks for Geeks
def GfG(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + GfG(arr[1:])
"""
Geeks for Geeks also suggests using "sum" in the python versions, but also offers this recursive form
This adds all the indexes of the array to the first [0] position and then calls the function in on itself starting using the second index [1].
Once there is only one index left all the previous indexes have been added to the first and therefore the sum is found in the only remaining index.
"""

#Main
def main():
    numArr = [random.randint(1,100) for index in range(1,11)]
    print(numArr)
    arrOFunctions = [myAttempt,GfG]
    for function in arrOFunctions:
        print(f"{function.__name__}: " + str(function(numArr)))

main()
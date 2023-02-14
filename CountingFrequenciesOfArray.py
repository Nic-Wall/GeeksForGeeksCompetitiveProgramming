import random
#My Attempt
def myAttempt(arr):
    tens = {}
    for i in arr:
        if i not in tens:
            tens[i] = 1
        else:
            tens[i] += 1
    return tens
"""
In this way every index of the array is accessed once. If it doesn't exist in the dictionary it is added as a key and given a value of one.
If the indexed value is already a key one more is added to value.

I'm speculating, based on the other solutions given by Geeks for Geeks, they will first sort the array, then find the start of each
index and count up until the index changes
ex.
[20,20,20,40,40,60,100]
20 starts at index 0 and continues until index 2 = 3
40 starts at 3 ends at 4 = 2
60 starts at 5 ends at 5 = 1
100 starts at 6 ends at 6 = 1
"""

#Geeks for Geeks
def GfG(arr):
    mp = {}
    for i in range(len(arr)):
        if arr[i] not in mp:
            mp[arr[i]] = 0
        mp[arr[i]] += 1
    return mp
"""
One of the best found solutions is similar to my own. Just without the else, because every element of the array will be counted once, the new keys to the dictionary
only need to be initialized once and then added onto. 
"""

#Main
def main():
    arr = [random.randrange(10,110,10) for i in range(0,100)]
    print(arr)
    arrOFunctions = [myAttempt,GfG]
    for function in arrOFunctions:
        print(f"{function.__name__}: " + str(function(arr)))

main()
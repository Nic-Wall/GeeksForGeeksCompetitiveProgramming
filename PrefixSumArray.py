import random
#My Attempt
def myAttempt(arr):
    arrSum = [arr[0]]
    for i in range(1, len(arr)):
        arrSum.append(arrSum[i-1] + arr[i])
    return arrSum
"""
My first attempt saw me looping through the input array, finding the previous sum of the arrSum array (by taking the last index)
then adding it to the arr index. Unfortunetly, I knew going in that this would require arrSum to be declared with at least one
or else an index error would occur. My first thought solution was to create the arrSum array with a 0 indexed in the 0th position
then remake the array at the end starting from the 1st position. While this works with only one loop if the input array is too large
recreating it without one index could take a while. Thanks to python lists being mutable I replaced the "arrSum = arrSum[1:]" line
with a .pop method.

Attempt 1
arrSum = [0]
    for i in arr:
        arrSum.append(arrSum[-1] + i)
    arrSum.pop(0)

I built on the program used by Geeks for Geeks to prevent any extra 0 from appearing on the array without mutatation.
"""

#Geeks for Geeks
def GfG(arr):
    prefixSum = [0 for i in range(len(arr)+1)]
    prefixSum[0] = arr[0]
    for i in range(1,len(arr)):
        prefixSum[i] = prefixSum[i-1] + arr[i]
    return prefixSum
"""
Geeks for Geeks selected "best" answer is similar to my own. It improves upon it by doing away with the pop through the creation
of the array with the 0th element of the input array. Then starting their loop from the 1st index. Unfortunetly, in the way the 
for loop is built, the program requires the loop is created with one extra index. This still requires the use of pop or other mutation. 
"""

#Main
def main():
    arr = [random.randint(1,10) for i in range(1,10)]
    print(arr)
    arrOFunctions = [myAttempt,GfG]
    for function in arrOFunctions:
        print(f"{function.__name__}: " + str(function(arr)))

main()
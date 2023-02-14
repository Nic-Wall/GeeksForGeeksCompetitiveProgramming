#My Attempt
def myAttempt(arr):
    Rarr = [-1 for i in arr]
    while len(arr)-1 not in Rarr:
        i = arr.index(min(arr))
        arr[i] = float("inf")
        Rarr[i] = max(Rarr) + 1
    return Rarr
"""
This was my first attempt:
Rarr = [0 for i in arr]
    counter = 0
    while len(arr)-1 not in Rarr:
        for i in range(0,len(arr)):
            if len(arr)-1 in Rarr:
                break
            elif min(arr) == arr[i]:
                arr[i] = float('inf')
                Rarr[i] = counter
                counter += 1
But I knew I could do better, hopefully down to one loop and without a counter.
Using the min and max methods I was able to slim it down to the following
Rarr = [-1 for i in arr]
    while len(arr)-1 not in Rarr:
        i = arr.index(min(arr))
        arr[i] = float("inf")
        Rarr[i] = max(Rarr) + 1
This would only cause the loop to run as many times as there were elements in the array. I don't know if this is cheating given my use of the index, max, and min methods.
    Especially because they must use some sorting algorithm of their own to find the max and min
"""

#Geeks for Geeks
def GfG(arr):
    n = len(arr)
    temp = [arr[i] for i in range (n) ]
     
    temp.sort()
     
    umap = {}
     
    val = 0
    for i in range (n):
        umap[temp[i]] = val
        val += 1
     
    for i in range (n):
        arr[i] = umap[arr[i]]

    return arr
"""
I think I understnad what they're attempting, but when ran it always returns an array full of 5's.
They first make a temporary array holding all the elements of the input array. Then sort the temp array min-max (so maybe using index, min, and max above wasn't cheating).
Then they create an empty dictionary and a counter(!)(the one thing I tried to avoid on my second attempt). Next creating a dictionary key of the array element with the increasing
counter. Since the array is sorted the value in the dictionary is the keys position position (smallest(0), second smallest (1), etc.). The value of the key is then put in 
it's proper place in the array. I wish it worked so I could compare speeds beyond Big O.
"""

#Main
def main():
        #  05 00  02  03  01  04
    arr = [50, 0, 20, 30, 10, 40]
    print(arr)
    arrOFunctions = [myAttempt,GfG]
    for function in arrOFunctions:
        print(f"{function.__name__}: " + str(function(arr)))

main()
import random
#My Attempt
def myAttempt(arr):
    holder = [float("inf"),-float("inf")]
    for i in arr:
        if(i > holder[1]):
            holder[1] = i
        elif(i < holder[0]):
            holder[0] = i
    return holder
"""
My first thought was to use a sorting algorithm (attempt #1) similar to bubble sort 
and return the first and last index... Until I saw it also requested for the task to 
be done in the least number of comparisons possible. So I tried attempt #2. In this way 
I only compare each value once instead of using the sorting array where each is compared 
AT LEAST once, maybe more. Using the python +-float("inf") I can create a max and min that will 
always be replaced no matter the number entered (so long as it's not another +-float("inf"). 
Of course the final, and simpliest, solution is to use the built-in min and max functions.

#Attempt 1
for i in range(len(arr)):
        for j in range(1, len(arr)+1):
            if(arr[i] > arr[-j]):
                arr[i], arr[-j] = arr[-j], arr[i]
            elif(arr[i] == arr[-j]):
                break
    return arr[0],arr[len(arr)-1]

"""

#Geeks for Geeks
def GfG(arr):
    n = len(arr)
    if(n % 2 == 0):
        mx, mn = max(arr[0],arr[1]), min(arr[0], arr[1])
        i = 2
    else:
        mx = mn = arr[0]
        i = 1
    while(i < n - 1):
        if arr[i] < arr[i + 1]:
            mx = max(mx, arr[i + 1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i + 1])
            i += 2
    return (mn, mx)
    

"""
The Geeks for Geeks example accounts for lists/ arrays the lengths of 1, 2, and 2<
In this way the function performs only one or only two comparisons. If there are more
than 2 indexes then the function performs a tournament style of comparisons, pitting
two individual indexes against each other until the max and min have been found.
I'm fairly confident I understand how it works, but the script hangsup on line 42
when ran. I'm not certain why
"""

#Main
def main():
    arr = [random.randint(1,100) for i in range(1,11)]
    print(arr)
    arrOFunctions = [myAttempt,GfG]
    for function in arrOFunctions:
        print(f"{function.__name__}: " + str(function(arr)))

main()
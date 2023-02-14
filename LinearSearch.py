#My Attempt
def myAttempt(arr,find, size):
    found = []
    for i in range(0,len(arr)//2):
        if arr[i] == find:
            found.append(i)
        if arr[-i-1] == find:
            found.append((-i * -1) + i)
    if len(arr) % 2 != 0:
        if arr[(len(arr)//2) + 1] == find:
            found.append((len(arr)//2) + 1)
    return found
"""
I know the easiest way to search would be from the front until the index is found. Like so...
for i in range(0,len(arr)):
    if arr[i] == find:
        return i
But so long as the sought after object is not in the middle it would be considerable faster to search from both sides as I did in my second attempt.
The only downside is if only one returned element is allowed. If the index is found on the latter side of the array first that is the one returned
even if there is a similar number indexed before that one.
Ex. arr = [10, 20, 80, 30, 60, 50, 110, 100, 110, 130, 170]
    find = 110
for i in range(0,len(arr)):
        if arr[i] == find:
            return i
        elif arr[-i-1] == find:
            return ((-i) * -1) + i
        else:
            pass
    return "Not Present"    #Blanket case if the item can't be found in the entered array
To account for this, I'll simply return an array every time (since GfG does not specify) and report the index of every finding. In this way I can improve
the script above by dividing the length in half and guarrenteeing the search of both halves. The example above will prevent every duplicate from being found if
arr[i] is found, even if the sought after integer is also present at arr[-i-1].
"""

#Geeks for Geeks
def GfG(arr,find, size):
    if(size == 0):
        return -1
    elif(arr[size-1] == find):
        return size - 1
    else:
        return GfG(arr,find,size - 1)
    return 0
"""
GfG only required the one element to be found and did not account for multiples of the sought after integer. Upon continuing to the next check I found I performed
something similar to a binary search, not a linear search... except in my first attempt
"""

#Main
def main():
    
    arr = [10, 20, 80, 30, 60, 110, 110, 100, 110, 130, 170, 80]
    find = 110
    size = len(arr)
    arrOFunctions = [myAttempt,GfG]
    for function in arrOFunctions:
        print(f"{function.__name__}: " + str(function(arr,find,size)))

main()
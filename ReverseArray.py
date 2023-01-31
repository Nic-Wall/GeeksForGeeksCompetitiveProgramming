#My First Attempt
def myAttempt(arr):
    newArr = []
    for index in range(1,len(arr)+1):
        newArr.append(arr[-index])
    return newArr
"""
I knew using a negative index in an array would reference the index furthest
from position 0 the closer it is from position 0.

Ex. 
arr[0] = 1, arr[1] = 2, etc.
but arr[-1] = 6

Using this I reversed the array by referencing the negative of each index!
"""

#Geeks for Geeks
def GfG(arr):
    return arr[::-1]
"""
Indexes in arrays can be referenced using colons.
For instance... 
arr[1:3] would display everything between index 1 and 3
arr[3:] would display everything up to the third index
arr[1:8:2] would display everything between index 1 and 3 in steps of 2
So Geeks for Geeks simply used arr[::-1] to reverse the array from the default first to last position by incrementals of -1
"""

#Main function
def main():
    inp = [index for index in range(1,7)]   #I made this myself :)
    print(inp)
    arrOFunctions = [myAttempt,GfG]
    for function in arrOFunctions:
        print(f"{function.__name__}: " + str(function(inp)))

main()


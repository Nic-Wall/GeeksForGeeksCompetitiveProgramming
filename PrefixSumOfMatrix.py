import random

#My Attempt
def myAttempt(arrMatrix):
    #prefixSum = [[0 for i in range(0,len(arrMatrix[0]))] for i in range(0, len(arrMatrix))]
    prefixSum = [[0 for i in range(0,len(arrMatrix[0])+1)]]   #Adding first row of zeros
    for i in range(0,len(arrMatrix)):                         #Adding column of zeros
        prefixSum.append([0])                                 #I would use "insert" but it doesn't work on arrays within arrays
        prefixSum[i+1] += arrMatrix[i]
    
    for row in range(0,len(arrMatrix)):
        for column in range(0,len(arrMatrix[0])):
            prefixSum[row+1][column+1] = prefixSum[row+1][column] + arrMatrix[row][column] + (prefixSum[row][column+1]           -  prefixSum[row][column])
                                         #Left number               #original number         #Top number (with all left + above)    #Removing all left of the column (to get it's original number) (see .txt for explanation)
    #removing the prefixSum[0] (the first array of 0s) and every 0 heading prefixSum[1:4]
    prefixSum = prefixSum[1:4]  #Removing the first array of 0s
    for i in range(0, len(prefixSum)):  #Removing the 0s heading the subsequent arrays
        prefixSum[i] = prefixSum[i][1:]
    return prefixSum
"""
https://usaco.guide/silver/more-prefix-sums?lang=cpp
I needed more of an explanation on how these worked ^
I started by adding a row and column of 0's so the loop wouldn't be out of range when adding the row/column index in a loop
My greatest struggle was finding the column prefix sum...
    prefixSum[row+1][column+1] = prefixSum[row+1][column] + arrMatrix[row][column]
this net me the row prefix sum of the rows
I was able to get the first column with the following...
    prefixSum[row+1][column+1] = prefixSum[row+1][column] + arrMatrix[row][column] + prefixSum[row][column+1]
But for subsequent columns it added the prefix sum from the row above, instead of the original row
From here I knew I needed to substract the rest of the prefix row to get only the original column number of the number above the soon to be prefix sum
    prefixSum[row+1][column+1] = prefixSum[row+1][column] + arrMatrix[row][column] + prefixSum[row][column+1] - sum(prefixSum[row][:column])
I found out the "sum(prefixSum[row][:column])" was removing extra. For instance asssume row 1 column 1 = 10 and row 1 column 2 = 30. Part of the 30 is the 10 next to it,
so summing the row up to the determined column was adding one extra 10. To fix this I simply removed the sum and changed the column to the int of the above column instead of all
ints up to that point. This gave me my final answer...
    prefixSum[row+1][column+1] = prefixSum[row+1][column] + arrMatrix[row][column] + (prefixSum[row][column+1]           -  prefixSum[row][column])
Now to remove the extra 0's...
This took me much longer than I would've liked, but having come to solution on my own provides such a rewarding feeling I can't help but be glad I spent the time figuring it out
"""

#Geeks for Geeks
def GfG(arrMatrix):
    n = len(arrMatrix)
    # vertical prefixsum
    for j in range(n):
        for i in range(1, n):
            arrMatrix[i][j] += arrMatrix[i - 1][j]
             
    # horizontal prefixsum
    for i in  range(n):
        for j in range(1, n):
            arrMatrix[i][j] += arrMatrix[i][j - 1]

    return arrMatrix
"""
Whereas I was attempting to solve the whole problem in one loop this clever user split the vertical and horizontal prefix sums of the matrix into two loop
They first start the loop on the horizontal axis going (prefixSum[column][row]) prefixSum[1][0], prefixSum[2][0], prefixSum[1][1], etc.
In this way the user avoids needing to substract the rest of the row as I did in my own
Then the horizontal portion, or rows, are calculated with the addition of the columns complete the user simply sums down the row at each column
Using this solution the user avoids the creation of unnecessary rows or columns of 0s
"""

#Main
def main():
    
    #arrMatrix = [[random.randint(1,10) for x in range(1,4)] for y in range(1,4)]
    arrMatrix = [[10,20,30],[5,10,20],[2,4,6]]
    print("2D Array Input:")
    for i in arrMatrix:
        print(i)
    arrOFunctions = [myAttempt,GfG]
    for function in arrOFunctions:
        print(f"\n{function.__name__}:")
        prefixSum = function(arrMatrix)
        for i in prefixSum:
            print(i)

main()
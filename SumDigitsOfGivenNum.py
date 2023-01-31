#My First Attempt
def myAttempt(UsIn):
    total = 0
    for num in str(UsIn):
        total += int(num)
    return total
"""
I knew strings could index individual characters so I reference each number individually by treating the input number as a string.
Then adding the single character number as an int into the total until each character in the input number is indexed.
My way works no matter the length of the string (so long as the sum isn't greater than 2,147,483,647) while the GfG example won't work on integers submitted to the function larger than max_int
"""

#Geeks for Geeks
def GfG(UsIn):
    total = 0
    while(UsIn != 0):
        total += int(UsIn%10)
        UsIn = int(UsIn/10)
    #return 0 if UsIn == 0 else int(UsIn % 10) + GfG(int(UsIn/10))    #This one line script calls itself until the parameter is equal to 0
    return total
"""
GfG first finds the remainder of UsIn/10, adds it to the total, then finds the divisible of UsIn by 10, and repeats until the input number is 0
Iteration   Calculation    Modulus     Total       UsIn
        1:  658 % 10       8            8          65
        2:   65 % 10       5           13           6
        3:    6 % 10       6           19           0
GfG's solution works backwards from my own as it is constantly adding the decimal remainder to the total
This way works recursively allowing for fewer lines typed and it doesn't have to change the type of the variable making it much more appealing in my eyes
I like it though, for the previous reasons and, it's an example of "thinking like a programmer" that helps change the way I analyze a problem and come to a solution
"""

#Main Function
def main():
    numberToSum = 658
    print(f"Input is: {numberToSum}")
    arrOFunctions = [myAttempt,GfG]
    for function in arrOFunctions:
        print(f"{function.__name__}: " + str(function(numberToSum)))

main()
#My Attempt
def myAttempt(word):
    return (word[::-1] == word)
"""
I now know from the "reverse array" question I can easily flip an array (and therefore a string) by index backwards in single step indexes.
Using this I can confirm or deny whether or not a string is a palindrome simply by comparing the word indexed in reverse with the word with a relational operator
"""

#Geeks for Geeks
def GfG(word):
    pass
"""
Geeks for Geeks only offers their solution in C
"""

#Main
def main():
    toRev = "racecar"
    print(f"{myAttempt.__name__}: " + str(myAttempt(toRev)))

main()
#This one is not on GfG, rather just a re-make of a school project

def printBoard(b):
    print("The board looks like the following...")
    print(f'   A   B   C\n  ____________\n | {b["A1"]} | {b["B1"]} | {b["C1"]}\n |---+---+---')
    print(f' | {b["A2"]} | {b["B2"]} | {b["C2"]}')
    print(f' |---+---+---\n | {b["A3"]} | {b["B3"]} | {b["C3"]}\n |---+---+---')

def main():
    opponentWin = False
    playerWin = False
    board = {"A1": 0, "B1":0, "C1":0,"A2": 0, "B2":0, "C2":0,"A3": 0, "B3":0, "C3":0}
    #count = int(input("Who goes first? 0 : you or 1 : AI?: "))
    count = 0
    while not playerWin and not opponentWin:
        printBoard(board)

        if(count % 2 == 0): #Player's turn
            playersChoice = input("P: ")
        else:   #AI's turn
            print()
        count += 1

        print(playersChoice)
        playerWin = True    #Remove after

main()

"""
"     A   B   C\n   ___________\n"
    " | {board("A1")} | {board("B1")} | {board("C1")}"
    "  |---+---+---"
Board
    A   B   C
   ___________
1 | X | X | X
  |---+---+---
2 | X | X | X
  |---+---+---
3 | X | X | X
"""
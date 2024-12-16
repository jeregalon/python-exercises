# tic tac toe game user vs. computer (uncomplete)

import random, math

board = [i + 1 for i in range(9)]
occupiedSquares = board[:]
board[4] = "X"
del occupiedSquares[4]
userTurn = True
gameComplete = False

def printBoard():
    for i in board:
        print(i)

def playGame():
    global userTurn, occupiedSquares
    
    while userTurn:
        numPlayed = 0
        try:
            numPlayed = int(input("Enter a number to play: "))
            if not (1 <= numPlayed <= 9):
                print("Not valid number. Try again")
            elif board.count(numPlayed) == 0:
                print("Occupied square. Try again")
            else:
                board[numPlayed - 1] = "O"
                userTurn = False
                printBoard()
        except ValueError:
            print("Please enter a valid character")
    else:
        randIndex = math.floor(random.random() * 9)
        if type(board[randIndex]) == int:
            print("My turn :)")
            board[randIndex] = "X"
            userTurn = True
            printBoard()
            print("I played ", randIndex + 1, " your turn.")
        else:
            pass


printBoard()


while not gameComplete:
    playGame()


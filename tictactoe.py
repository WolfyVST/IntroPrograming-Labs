# CMPT 120 Intro to Programming
# Lab #7 – Lists and Error Handling
# Author: Ricardo villalobos
# Created: 4/25/2020
symbol = [ " ", "x", "o" ]
#def printRow(row):
 #print(" | ",row[1]," | ",(" | ",row[2]," | ",(" | ",row[3])
 #pass
def printBoard(board):
 print("+-----------+")
 print(" | ",board[0]," | "," | ",board[1]," | "," | ",board[2], "|")
 print  ("+-----------+")
 print(" | ",board[3], " | ", " | ",board[4], " | ", " | ",board[5], "|")
 print("+-----------+")
 print(" | ",board[6], " | ", " | ",board[7], " | ", " | ",board[8], "|")
 print("+-----------+")

def markBoard(board, row, col, player):
  # check to see whether the desired square is blank
  # if so, set it to the player number
 pass
def getPlayerMove():
 input("") # prompt the user separately for the row and column numbers
 return (0,0) # then return that row and column instead of (0,0)
def hasBlanks(board):
 ban = 0
 for i in range(0,9):
  if board[i] == "":
   ban = ban +1
  else:
   ban = ban + 0
 if ban == 9:
  return True
 else:
  return False
 # for each row in the board...
 # for each square in the row...
 # check whether the square is blank
 # if so, return True
 # if no square is blank, return False


def main():
 board = []
 player = 1
 while hasBlanks(board):
    printBoard(board)
 row, col = getPlayerMove()
 markBoard(board, row, col, player)
 player = player % 2 + 1  # switch player for next turn
main()

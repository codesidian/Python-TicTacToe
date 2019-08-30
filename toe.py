import os

class Board():
        def __init__(self):
                self.spaces = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

        def getBoard(self):
                return self.spaces

        def occupySpace(self,char,space):
                #top row
                if(space == 'tl'):
                        self.spaces[0][0] = char
                elif(space == 'tm'):
                        self.spaces[0][1] = char
                elif(space == 'tr'):
                        self.spaces[0][2] = char
                #middle row
                if(space == 'ml'):
                        self.spaces[1][0] = char
                elif(space == 'mm'):
                        self.spaces[1][1] = char
                elif(space == 'mr'):
                        self.spaces[1][2] = char
                #bottom row
                if(space == 'bl'):
                        self.spaces[2][0] = char
                elif(space == 'bm'):
                        self.spaces[2][1] = char
                elif(space == 'br'):
                        self.spaces[2][2] = char

                return None

class toe():
        def __init__(self):
                self.gameBoard = Board()

        def printBoard(self):
                spaces = self.gameBoard.getBoard()
                print(spaces[0][0]+'|'+spaces[0][1]+'|'+spaces[0][2])
                print('-----')
                print(spaces[1][0]+'|'+spaces[1][1]+'|'+spaces[1][2])
                print('-----')
                print(spaces[2][0]+'|'+spaces[2][1]+'|'+spaces[2][2])



        def playTurn(self,char,space):
                self.gameBoard.occupySpace(char.upper(),space.lower())

                return None

        def hasWinner(self):
                result = False
                winner = 'no one'
                currentBoard = self.gameBoard.getBoard()

                if(currentBoard[0][0] == currentBoard[1][0] == currentBoard[2][0] != ' '):
                        winner = currentBoard[0][0]
                        result = True
                elif(currentBoard[0][1] == currentBoard[1][1] == currentBoard[2][1] != ' '):
                        winner = currentBoard[0][1]
                        result = True
                elif(currentBoard[0][2] == currentBoard[1][2] == currentBoard[2][2] != ' '):
                        winner = currentBoard[0][2]
                        result = True
                elif(currentBoard[0][0] == currentBoard[0][1] == currentBoard[0][2] != ' '):
                        winner = currentBoard[0][0]
                        result = True
                elif(currentBoard[1][0] == currentBoard[1][1] == currentBoard[1][2] != ' '):
                        winner = currentBoard[1][0]
                        result = True
                elif(currentBoard[2][0] == currentBoard[2][1] == currentBoard[2][2] != ' '):
                        winner = currentBoard[2][0]
                        result = True
                elif(currentBoard[0][0] == currentBoard[1][1] == currentBoard[2][2] != ' '):
                        winner = currentBoard[0][0]
                        result = True
                elif(currentBoard[2][0] == currentBoard[1][1] == currentBoard[0][2] != ' '):
                        winner = currentBoard[2][0]
                        result = True
                elif( not ' ' in (spaces[0] for spaces in currentBoard)):
                        winner = 'No One'
                        result = True
                        
                return [result,winner]



game = toe()
isWin,winChar = game.hasWinner()
instructions = "Enter where you'd like to go (tl,tm,tr,ml,mm,mr,bl,bm,br), followed by your character (X | O)"

print("####### TIC TAC TOE ######")
game.printBoard()
print(instructions)
while(not isWin):
        location,char = input('').split(' ')
        _=os.system("cls")
        game.playTurn(char,location)
        print("####### TIC TAC TOE ######")
        game.printBoard()
        print(instructions)
        isWin,winChar = game.hasWinner()
        if(isWin):
                print('Result: ' + winChar + ' wins')
_=input()

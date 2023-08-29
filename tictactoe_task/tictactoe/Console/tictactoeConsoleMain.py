"""
This module is the main console application for the tictactoe game.

It also contains two functions that is called by the main console application.

playAgain()
promptGoFirst()
"""

from tictactoe.tictactoeFactory import tictactoeFromConsoleBuilder
from tictactoe.tictactoeEnums import gameState, playerTurn
from tictactoe.tictactoeGrid import tictactoeGrid

def main():
    pass

if __name__ == '__main__':
    main()

"""
The following are internal variables for documentation purposes only.
"""

__author__ = "Sec Chu"
__author_email__ = "duongchu@hotmail.com"
__comments__ = "Developed during my study at QA Bootcamp as part of my portfolio"
__license__ = "No Licensing restrictions in place. Feel free to use code as you wish"


def playAgain():
    """
    This function prompts the user if they wish to play again.

    User is prompted within a loop if the input is invalid. Acceptable
    inputs are y, Y, n or N.

    Parameters
    ==========
    There are no parameters for this function

    Return
    ======
    The function does not explicitly return any values so None is returned
    by default.

    Raises
    ======
    The input function can raise an error if cancel is pressed.
    """

    while True:
        again = input("Play again?: ")

        again = again.upper()

        if again == "Y" or again == "N":
            return again

        print("Enter Y or N")

def promptGoFirst():
    """
    This function prompts the user if they wish to go first.

    User is prompted within a loop if the input is invalid. Acceptable
    inputs are y, Y, n or N.

    Parameters
    ==========
    There are no parameters for this function

    Return
    ======
    The function does not explicitly return any values so None is returned
    by default.

    Raises
    ======
    The input function can raise an error if cancel is pressed.
    """

    while True:
        choice = input("Do you want to go first?")
        choice = choice.upper()

        if choice == "Y" or choice == "N":
            return choice

        print("Please enter Y or N")

"""
Main execution of the tictactoe console application
"""
gameBuilder = tictactoeFromConsoleBuilder()
while True:

    choice = input("Press q to quit and any other key to continue")

    if choice == "q":
        break

    #Get user to input the game preferences via console prompts
    gameConfig = gameBuilder.getGameConfig()

    #Player 1 is always console and playerType.Console is the default value
    p1, p2, board = gameBuilder.createGame(player1=gameConfig[0], p1goFirst=gameConfig[1],
                                          p2Type=gameConfig[2])
    while True:
        players = (p1, p2)

        currentTurn = 0
        if board.turn == p2.turn:
            currentTurn = 1

        print(board.renderedGrid)
        while board.CurrentState == gameState.Incomplete:
            players[currentTurn].placeMove()
            print(board.renderedGrid)
            currentTurn = (currentTurn + 1) % 2

        board.verifyEndGameIntegrity()
        again = playAgain()

        if again == "N":
            break

        goFirst = promptGoFirst()

        if goFirst == "Y":
            board.new_game(playerTurn.Player1)
        else:
            board.new_game(playerTurn.Player2)









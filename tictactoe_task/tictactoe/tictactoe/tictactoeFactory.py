"""
This module contains the TictactoeGameBuilder class which is an abstract class
that represents a factory builder class that creates the tictactoe game components
required in a tictactoe game. A game will require two player objects using the same
tictactoe grid object.
"""

from tictactoe.tictactoeGrid import tictactoeGrid
from Players.ConsolePlayer import ConsolePlayer
from Players.RandomPlayer import RandomPlayer
from tictactoe.tictactoeEnums import playerTurn
from abc import ABC, abstractmethod
from tictactoe.tictactoeEnums import playerType

class TictactoeGameBuilder(ABC):

    @abstractmethod
    def getGameConfig(self):
        """
        This is a abstract method for getting the tictactoe game settings
        """
        pass

    @staticmethod
    def __factoryCreatePlayer__(grid, turn, pType=playerType.Console):
        """
        This is a static method for creating a tictactoe player object.

        Parameters
        ==========
        grid is the tictactoeGrid object that should be used by the created player.

        turn is a playerTurn Enum object representing the player to make the first move.
        playerTurn.Player1 is 'O' and playerTurn.Player2 is 'X'.

        pType is an enum representing the required player type to be created. playerType.Console represents
        a ConsolePlayer while playerType.Random represents a RandomPlayer.
        """
        if pType == playerType.Console:
            return ConsolePlayer(grid, turn)
        else:
            return RandomPlayer(grid, turn)

    def createGame(self, player1, p1goFirst, p1Type = playerType.Console, p2Type = playerType.Console):
        """
        Method that returns all the gaming components required in a tictactoe game. This is two players
        sharing a tictactoeGrid.

        Parameters
        ==========
        player1 is of type playerTurn that represents playerTurn.Player1 or playerTurn.Player1 depending
        on the selection of player 1. Player 1 is the users selected player and it always be console. This
        argument will decide whether it has 'O' or 'X'. playerTurn.Player1 will represent 'O'.

        p1goFirst is a boolean variable representing if player1 will go first. It should be True if player 1
        goes first otherwise it should be False.

        p1Type is the player type of player 1. Even though this function allows you to select a different type
        for player 1 it is always console and Random Player for player 1 is never used.

        p2Type is the player type for player 2. It can be Console or Random Player.

        Return
        ======
        Method returns a tuple that contains both player objects and the tictactoeGrid object required in a tictactoeEnums
        game.
        """
        player2 = playerTurn((player1.value + 1) % 2)

        playerToMoveFirst = None
        if p1goFirst:
            playerToMoveFirst = player1
        else:
            playerToMoveFirst = player2


        grid = tictactoeGrid(playerToMoveFirst)

        p1 = TictactoeGameBuilder.__factoryCreatePlayer__(grid, player1, p1Type)
        p2 = TictactoeGameBuilder.__factoryCreatePlayer__(grid, player2, p2Type)

        #If the demo app gets any more complicated we would have to create a separate class
        #that embeds player1, player2 and grid such as a game. This is fine for the task.
        return (p1, p2, grid)

class tictactoeFromConsoleBuilder(TictactoeGameBuilder):
    """
    This class inherits from the TictactoeGameBuilder class and overrides the getGameConfig
    abstract method.
    """

    def getGameConfig(self):
        """
        This method simply calls the static method __fromConsole__ that gets all
        the gaming parameters prompted from the user at the console.

        Parameters
        ==========
        None

        Returns
        =======
        Method returns a tuple of all the gaming settings chosen by the user at the console.
        """
        return tictactoeFromConsoleBuilder.__fromConsole__()

    @staticmethod
    def __fromConsole__():
        """
        This static method prompts the user for all the gaming parameters
        for the tictactoe game.

        Parameters
        ==========
        None

        Returns
        =======
        Method returns a tuple of all the gaming settings chosen by the user at the console.
        """
        player1 = tictactoeFromConsoleBuilder.__getPlayerSelection__()
        p1goFirst = tictactoeFromConsoleBuilder.__getTurnFromConsole__()
        p2Type = tictactoeFromConsoleBuilder.__getPlayerType__()

        return (player1, p1goFirst, p2Type)

    @staticmethod
    def __getPlayerSelection__():
        """
        Static method that prompts the user for their chosen symbol from the console.

        Parameters
        ==========
        None

        Returns
        =======
        Returns a playerTurn Enum representing the chosen symbol. playerTurn.Player1
        represents 'O' and playerTurn.Player2 represents 'X'. Method will continuously
        validate invalid input until it is valid and acceptable.
        """

        while True:
            symbol = input("Which symbol would you like, X or O: ")
            symbol = symbol.upper().strip()
            success, msg = tictactoeFromConsoleBuilder.__validateSymbol__(symbol)

            print(msg)
            if success:
                return playerTurn(int(symbol.upper().strip() == "X"))

    @staticmethod
    def __getTurnFromConsole__():
        """
        Static method to prompt the user whether they choose to go first.

        Parameters
        ==========
        None

        Returns
        =======
        Method returns True if player 1 chooses to go first or False otherwise.
        Method will continuously validate invalid input until it is valid and
        acceptable.
        """
        while True:
            userInput = input("Would you like to go first. Enter Y or N: ")
            success, goFirst, msg = tictactoeFromConsoleBuilder.__validateTurn__(userInput)

            print(msg)

            if success:
                return goFirst

    @staticmethod
    def __validateTurn__(userInput):
        """
        This method validates the user input for whether they wish to go first.

        Parameters
        ==========
        userInput is a string representing the user input entered on the console.

        Returns
        =======
        Method will return a tuple of three elements. The first element is a boolean
        value representing whether is input is valid and accepted. The first element
        should return True if the input is valid otherwise it should return False.

        The second element should be a boolean value representing if the player has
        chosen to go first. True if player chooses to go first or False otherwise. Note
        the value will be None if the input is invalid.

        The final element of the tuple should be a string that should be returned to the
        user. This would either be a success message or an error message letting the user
        know the input is invalid.
        """

        if userInput is None:
            return (False, False, "Unexpected error!")

        userInput = userInput.upper().strip()

        if userInput != 'Y' and userInput != 'N':
            return (False, None, "Please enter Y or N. Try again!")

        if userInput == 'Y':
            return (True, True, "OK you go first")

        return (True, False, "OK you go second")

    @staticmethod
    def __validateSymbol__(symbol):
        """
        Static method that validates the user input for their chosen symbol.

        Parameters
        ==========
        symbol is the console input entered by the user on the console for their chosen symbol.

        Returns
        =======
        Method returns a tuple of two elements. The first element is a boolean value
        to indicate if the input was valid and the symbol was successfully parsed. True
        if valid or False otherwise.

        The second element of the tuple should be a string that should be returned to the
        user. This would either be a success message or an error message letting the user
        know the input is invalid.

        """
        if(symbol is None):
            return (False, "Unexpected error!")

        symbol = symbol.upper().strip()
        if symbol != 'X' and symbol != 'O':
            return (False, "Try again. Symbols can only be O or X")

        return (True, f"You got it. you are {symbol}")

    @staticmethod
    def __getPlayerType__():
        """
        This static method prompts the user for their chosen type on the console.

        Parameters
        ==========
        None

        Returns
        =======
        Method returns a boolean value indicating whether the input was valid and if their
        choice was accepted.
        """
        while True:
            print("Who would you like to play")
            print("1: Random Player")
            print("2: Another Player using the console")
            userInput = input("Enter 1 for Random Player or 2 for Console Player")

            success, choice, msg = tictactoeFromConsoleBuilder.__validatePlayerInput__(userInput)

            print(msg)

            if success:
                #return the enum type of the selected player type choice
                return choice

    @staticmethod
    def __validatePlayerInput__(userInput):
        """
        Method validates the user input for their selected player type

        Parameters
        ==========
        userInput is the string representing the user input entered on the console

        Returns
        =======
        Method returns a tuple of three elements. The first element is a boolean value
        that is True if the input was valid and their choice was successfully parsed or
        False otherwise.

        The second element is the player type returned as an Enum of playerType which can be playerType.Console for
        Console Player and playerType.Random for Random Player. Note it can be None if the input is invalid and can't
        be understood.

        The final element of the tuple should be a string that should be returned to the
        user. This would either be a success message or an error message letting the user
        know the input is invalid.
        """
        if(userInput is None):
            return (False, None, "Unexpected error!")

        userInput = userInput.strip()

        if userInput == "1":
            return (True, playerType(int(userInput)), "You will be playing against a Random Player")
        elif userInput == "2":
            return (True, playerType(int(userInput)), "You will be playing against a Console Player")
        else:
            return (False, None, "Error! Enter 1 for Random Player or 2 for Console Player. Try again!")









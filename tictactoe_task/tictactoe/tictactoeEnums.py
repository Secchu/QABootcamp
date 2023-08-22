"""
This module contains all the Enum type classes used in the tictactoe console application.
"""

from enum import Enum

class playerTurn(Enum):
    """
    Enum class that represents the players turn. These
    are static values
    """
    Player1 = 0
    Player2 = 1

    def __str__(self):
        """
        Method returns a string of the value of a playerTurn Enum object when it is
        converted to string
        
        Parameters
        ==========
        None
        
        Returns
        ======
        Method returns a string of the value of a playerTurn Enum object when it is
        converted to string
        """
        strings = ("Player 1", "Player 2")

        return strings[self.value]

class gameState(Enum):
    """
    gameState is an Enum class representing the state of a tictactoe game.
    
    Below are static values of the possible enum values.
    """
    Player1Win = 1
    Player2Win = 2
    Incomplete = 0
    Draw = 3

    def __str__(self):
        """
        Method that returns the possible string values of the gameState Enum when it is
        converted to string.
        
        Parameters
        ==========
        None
        
        Returns
        ======
        Method that returns the possible string values of the gameState Enum when it is
        converted to string.
        """
        strings = {0: "Incomplete", 1: "Player 1 Win", 2: "Player 2 Win", 3:"Draw"}

        return strings[self.value]

class gridState(Enum):
    """
    gridState is an Enum class representing the state of a grid on a tictactoe grid.
    
    Below are static values of the possible enum values.
    """
    GridFree = 0
    Player1 = 1
    Player2 = 4

class playerSymbol(Enum):
    """
    playerSymbol is an Enum representing the possible symbols used in a tictactoe game. 
    This can be 'O' or 'X'. There is also Unoccupied is takes the value of an empty string.
    """
    Player1 = "O"
    Player2 = "X"
    Unoccupied = " "

    def __str__(self):
        return self.value

class playerType(Enum):
    """
    This Enum class represents the player type which can be Random player
    or a console player.
    """
    Random = 1
    Console = 2


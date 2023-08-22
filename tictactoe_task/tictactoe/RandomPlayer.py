"""
This class represents an automated tictactoe Player that selects their move randomly.

RandomPlayer inherits from an abstract class called tictactoePlayer. It overrides the
abstract method getMove. getMove simply generates a random number from a list of 
available moves.
"""

from tictactoePlayer import tictactoePlayer
from random import randint

class RandomPlayer(tictactoePlayer):
    def __init__(self, board, turn):
        super().__init__(board, turn)

    def getMove(self):
        """
        It overrides the abstract method getMove. getMove simply generates a random number from a list of 
        available moves.
        
        Parameters
        ==========
        Method does not have any input parameters
        
        Returns
        =======
        Returns the selected move in the single integer format in which the 9 tictactoe grids are represented
        by a number 1 to 9.
        """
        available = self.board.AvailableMoves
        return available[randint(0, len(available) - 1)]

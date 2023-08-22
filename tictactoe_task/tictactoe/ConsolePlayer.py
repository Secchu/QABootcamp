"""
This module contains the ConsolePlayer class which represents a tictactoe player that uses 
the console to play tictactoe. 

It also contains a function called withinRange that is used for validation of ints.
"""

from tictactoePlayer import tictactoePlayer
from tictactoeGrid import tictactoeGrid

def withinRange(lower, upper, var):
    """
    Function validates an int is within the range of lower and upper limits. Even though function
    was originally designed for validating ints it does work for string data types or even floats.
    Infact it is a flexible function that can work with any data types that work with relational
    operators. The three data types should be of the same type.
    
    Parameters
    ==========
    lower is an variable that represents the inclusive lower limit.
    
    upper is an variable that represent the inclusive upper limit.
    
    var is the variable being tested for the lower and upper limit inclusively.
    
    Note function will assume the inputs are of the same type and there is no error handling or type
    checking within the function. It is the callers responsibility to make sure all inputs are of the 
    same type.
    
    Return
    ======
    Returns True if var is within the range of lower and upper inclusively. Otherwise returns False.
    
    Raises
    ======
    Function will raise an error if any of the inputs can not be used with the <= or >= operator.
    """
    return var >= lower and var <= upper

class ConsolePlayer(tictactoePlayer):
    
    """
    This class represents a tictactoe player using the console to play tictactoe. It inherits
    from the abstract tictactoePlayer class and overrides the getMove method.
    """
    
    def __init__(self, board, turn):
        """
        Initializer calls the base initializer
        
        Parameters
        ==========
        board represents the tictactoe grid and is of type tictactoeGrid. Note the board must have the
        same reference as the opposing player for both players to play against eachother. In otherwords
        the id() function should return the same value which usually does when two object references 
        point to the same object.
        """
        super().__init__(board, turn)

    def getMove(self):
        """
        The getMove method is overridden by the ConsolePlayer class. This method simply gets the move
        from the player by prompting the move on the console.
        
        Note the move is continuously prompted until the input is valid. The move prompted is in the row
        column format and only integer strings are acceptable. The row and column input is separated by
        spaces.
        
        Parameters
        ==========
        The method accepts no input parameters
        
        Return
        ======
        Function does not return any values explicitly so None is returned by default.
        
        Raises
        ======
        The input function can raise an error if cancel is pressed.
        """

        #if self.turn != self.board.turn:
        #    raise NotYourTurnError("You can only move when it is your turn")

        while True:

            #The task asks for the row and column to be inputted. If I had a choice I would
            #get them to input the grid number directly
            userInput = input("Please enter row and column separated by space: ")

            gridNo, msg = ConsolePlayer.parseAndValidateMove(userInput, self.board.AvailableMoves)
            print(msg)

            if gridNo is not None:
                return gridNo

    @staticmethod
    def parseAndValidateMove(string, available):
        """
        This is a static function that accepts the users input moves as a string and validates the inputted move.
        
        Parameters
        ==========
        string is the move inputted by the console player.
        
        available is an interable that represents the available moves. It is used by the function to validate the move
        selected is available. It is the callers responsibility that the parameter is accurate and does reflect the
        available moves that can be selected by the user. Note that the available move is in the single integer format
        meaning each grid is represented from 1 to 9. For example the first grid on the upper left corner is 1. The middle
        grid is 5. The grid on the lower right corner is 9.
        
        Return
        ======
        The function will return a tuple with two elements. The first element of the tuple is grid number that represents
        the console players move from integers 1 to 9. If the move selected was invalid or not available than None is returned.
        The second element of the tuple represents console output. This would either be a validation message or a message to
        the user informing them that their move has been accepted.
        """
        if string == None:
            return (None, "Unexpected error!")

        ints = string.split(' ')

        if len(ints) < 2:
            return (None, "Error! Its row and column separated by spaces. Try again!")

        if not ints[0].isnumeric() or not ints[1].isnumeric():
            return (None, "Rows and column must be in numeric format try again!")

        row = int(ints[0])
        col = int(ints[1])

        if not withinRange(1, 3, row) or not withinRange(1, 3, col):
            return (None, "Row and column has to be with the range of 1-3. Try again!")

        gridNo = tictactoeGrid.getGridNoFromRowCol(row, col)

        if gridNo not in available:
            return (None, "This grid has already been occupied. Please try again!")

        return (gridNo, "Your move has been accepted!")



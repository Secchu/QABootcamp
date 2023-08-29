from tictactoe.tictactoeLineCombo import tictactoeLineCombo,  affectedLinesByGrid
from tictactoe.tictactoeEnums import playerTurn, gameState, gridState, playerSymbol
from tictactoe.tictactoeErrors import gridOccupiedError, gameAlreadyCompletedError, InvalidEndGameState

"""
Class tictacetoeGrid represents the tic tac toe grid and game state.

    =============================
    |    1    |    2    |    3   |
    =============================
    |    4    |    5    |    6   |
    =============================
    |    7    |    8    |    9   |
    =============================

The grid squares are represented by numbers 1 to 9 are keys in a dictionary. The values in a dictionary
represents players move. This is represented by move.
Player moves represented by
0 : empty grid
1 : player 1
4 : player 2

Why is player 2 4 and not 2? I am not complicating things here. We can work out a win as follows
player 1 win : sum of line is 3
player 2 win : sum of line is 12
draw: all grids are occupied or have a value above zero

"""

class tictactoeMove:
    """
    Class that represents a tictactoe's player last move
    """
    def __init__(self, player, move):
        """
        Initializer that initalise the initial values of player
        and move.

        __player__ is the player that made the last move. This is an internal variable. You
        should not access this variable directly but use the property player to access the
        value of this variable.

        __move__ represent the last move made by the last player. It is an integer that represents the
        chosen grid labelled from 1 to 9. This is also an internal variable. You
        should not access this variable directly but use the property move to access the
        value of this variable.
        """
        self.__player__ = player
        self.__move__ = move

    @property
    def player(self):
        """
        player getter representing the last player to make the last move
        """
        return self.__player__

    @property
    def move(self):
        """
        move getter should represent the last move made by the last player. It is an integer that represents the
        chosen grid labelled from 1 to 9.
        """
        return self.__move__



class tictactoeGrid:
    """
    This class represents the tictactoe grid

    template is the intial rendered grid string used by the property renderedGrid. Everytime
    new_game is called the renderedGrid property is reset to the initial template.
    """

    template = """
    =============================
    |    1    |    2    |    3   |
    =============================
    |    4    |    5    |    6   |
    =============================
    |    7    |    8    |    9   |
    =============================
{}"""

    def __init__(self, turn = playerTurn.Player1):
        """
        Initializer that initializes all the possible values of the __symbols__ variable and then
        new_game is called to initialize all other variables.
        """
        self.__symbols__ = (playerSymbol.Player1, playerSymbol.Player2, playerSymbol.Unoccupied)
        self.new_game(turn = turn)


    #This property should be read only private access. Convention is internal properties have underscore.
    def __setturn__(self, turn):
        """
        This method sets the turn of the next player to make a move. You should not access this
        variable through this internal function but use the turn getter property if you need to
        access this value.
        """
        if not isinstance(turn, playerTurn):
            raise TypeError(f"turn should be {playerTurn} enum and not {type(turn)}")

        self.turn = turn

    def __currentSymbol__(self):
        """Return the symbol to be used for the next move"""
        return self.__symbols__[self.turn.value]

    def new_game(self, turn = playerTurn.Player1):

        """
        This method srarts a new tictactoe game

        Parameters
        ==========
        turn is a playerTurn Enum representing the player that should make the first move.

        Returns
        =======
        The method does not explicitly return any value so None is returned by default.

        Raises
        ======
        Method returns a TypeError if parameter turn is not of type playerTurn. It is the
        callers responsibility to make sure the correct type is passed.
        """

        self.__setturn__(turn)

        #Because the game hasn't started therefore the second argument is None
        #to signify a move has yet to be made
        self.__lastMove__ = tictactoeMove(self.turn, None)

        self.__totalMoves__ = 0
        self.__gameState__ = gameState.Incomplete
        self.__grid__ = dict(zip(range(1, 10), [0] * 9))

    def make_move(self, move):
        """
        This method places the move for the next player. You should not call this method
        directly. You should use one of the player classes such as ConsolePlayer and
        RandomPlayer and call getMove which in turn calls make_move on the grid.

        Parameters
        ==========
        move is an integer representing the players move. It should be an integer from 1 to 9
        with each number representing the tictactoe grid. The move is best illustrated with the
        diagram below.

    =============================
    |    1    |    2    |    3   |
    =============================
    |    4    |    5    |    6   |
    =============================
    |    7    |    8    |    9   |
    =============================

        Returns
        =======
        The method does not explicitly return any value so None is returned by default.
        Method does not keep track of the players turn. Use the turn property to get the
        next players turn.

        Raises
        ======
        An error will be raised if move is out of range

        """
        if(self.__totalMoves__ >= 9 or self.__gameState__ != gameState.Incomplete):
            raise gameAlreadyCompletedError("Game has already completed")

        if(self.__grid__[move] > 0):
            raise gridOccupiedError(f"Grid {move} has already been occupied")

        #Sum of moves inclusive of both player
        self.__totalMoves__ += 1

        #Make move
        self.__grid__[move] = self.turn.value * 3 + 1

        self.__lastMove__ = tictactoeMove(self.turn, move)
        currentTurn = playerTurn((self.turn.value + 1) % 2)
        self.__setturn__(currentTurn)

        #Minimum moves required for a win is 5 moves inclusive of both players
        if self.__totalMoves__ >= 5:
            self.__gameState__ = self.__checkPlayerWinMove__(move)

    @property
    def renderedGrid(self):

        symbols = {0:playerSymbol.Unoccupied, 1:playerSymbol.Player1, 4:playerSymbol.Player2}
        #grid = self.__template__
        grid = tictactoeGrid.template
        for x in range(1, 10):
            gridValue = self.grid[x]
            grid = grid.replace(str(x), symbols[gridValue].value)

        return grid.format(self.CurrentGameMsg)


    def __checkPlayerWinMove__(self, move):
        """
        Method to check if player made a winning move. As a shortcut it only checks for line combos
        that are winnable from the move. Also the Method does not fully check for draw. It just assumes
        a draw if the move does not result to a win and the total moves equates to 9.

        This method should be private therefore by convention the name begins and ends with double underscore.

        Also the method verifyEndGameIntegrity performs a full check for game result. The method should be called
        once and also performs a final check for game integrity.
        """

        """
        WIN_LINES = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],  # horiz.
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],  # vertical
        [1, 5, 9],
        [3, 5, 7],  # diagonal
    ]

        Get the indexes of the winnable line combos. For example if move is 7 then indexes is (2, 3, 7)
        """
        lineIndexes = affectedLinesByGrid[move]

        #Using the indexes extract the minimal lines for the check. We don't check all lines but only the lines winnable from
        #the players move
        winnableCombos = (tictactoeLineCombo.WIN_LINES[index] for index in lineIndexes)

        for combo in winnableCombos:
            #The line are keys to the grid dictionary that make up the winning line combo
            lineSum = sum((self.__grid__[combo[0]], self.__grid__[combo[1]], self.__grid__[combo[2]]))
            if(lineSum == 3):
                return gameState.Player1Win
            if(lineSum == 12):
                return gameState.Player2Win

        #If there is no win and total moves is 9 then assume draw. You can use verifyEndGameIntegrity()
        #to check for end game integrity if desired.
        if(self.__totalMoves__ == 9):
            return gameState.Draw

        return gameState.Incomplete

    def gridState(self, gridNo):
        return gridState(self.__grid__[gridNo])

    @staticmethod
    def getGridNoFromRowCol(row, col):
        """
        Funcion to return grid number from row and column number

                | col 1 | col 2 | col 3 |
        ===================================
         row 1  |   1   |   2   |   3   |
        ===================================
         row 2  |   4   |   5   |   6   |
        ===================================
         row 3  |   7   |   8   |   9   |
        ===================================
        """
        return row * 3 - 3 + col

    @staticmethod
    def getRowColFromGridNo(gridNo):
        """
        Static Method that returns grid a tuple in the form (row, col) from the grid number.
        Method accepts gridNo as function input.

                | col 1 | col 2 | col 3 |
        ===================================
         row 1  |   1   |   2   |   3   |
        ===================================
         row 2  |   4   |   5   |   6   |
        ===================================
         row 3  |   7   |   8   |   9   |
        ===================================

        For example if grid number is 2 then method returns (1, 2) as 2 is in row 1 and col 2.
        Another example if grid number is 7 then method returns (3, 1) as 7 is in row 3 and col 1.
        """
        return ((gridNo - 1) // 3 + 1, (gridNo - 1) % 3 + 1)

    @property
    def grid(self):
        return self.__grid__

    def verifyEndGameIntegrity(self):
        """
        Method to verify and confirm that the game state has completed and that there are no errors.
        1. If the game has been won by a player then there should only be 1 winning line.
        2. If the game is a draw then there should be no winning lines and all grids are occupied (not zero).
        3. If the method is called when the game is incomplete an exception is thrown.

        Parameters
        ==========
        None

        Returns
        =======
        The method does not explicitly return any value so None is returned by default.

        Raises
        ======
        If an logical error is detected in the game state an InvalidEndGameState is raised.
        """

        if self.__gameState__ == gameState.Incomplete:
            raise InvalidEndGameState("Method should not be called for incomplete game")


        totalPlayer1Combo = 0
        totalPlayer2Combo = 0

        for line in tictactoeLineCombo.WIN_LINES:
            combo = [self.__grid__[line[0]], self.__grid__[line[1]], self.__grid__[line[2]]]
            lineSum = sum(combo)
            if lineSum == 3:
                totalPlayer1Combo += 1
            elif lineSum == 12:
                totalPlayer2Combo += 1

        #It is possible to win a tictactoe game with maximum of two lines. Regardless the opponent will have zero win
        #lines
        if self.__gameState__ == gameState.Player1Win:
            if totalPlayer2Combo > 0:
                raise InvalidEndGameState("Logical error detected! Total number of win lines not adding up")
            if totalPlayer1Combo < 1 or totalPlayer1Combo > 2:
                raise InvalidEndGameState("Logical error detected! Total number of win lines not adding up")

        if self.__gameState__ == gameState.Player2Win:
            if totalPlayer1Combo > 0:
                raise InvalidEndGameState("Logical error detected! Total number of win lines not adding up")
            if totalPlayer2Combo < 1 or totalPlayer2Combo > 2:
                raise InvalidEndGameState("Logical error detected! Total number of win lines not adding up")

        if self.__gameState__ == gameState.Draw:
            if totalPlayer1Combo != 0 or totalPlayer2Combo != 0:
                raise InvalidEndGameState("Logical error detected! There should no be winning lines in a draw")
            if 0 in self.__grid__.values():
                raise InvalidEndGameState("Logical error detected! Game is draw but there are still empty grids")
            if self.__totalMoves__ != 9:
                raise InvalidEndGameState("Logical error detected! Total moves in a draw should be 9")

        #Lets count the total moves of each player and take the difference. It is possible for 1 player to have
        #made atmost 1 more move than the other. Initially I used count() for this but found out that I was iterating
        #the dictionary values twice therefore manually programmed the iteration.

        totalR1Move = 0
        totalR2Move = 0
        for sq in self.grid.values():
            if sq == 1:
                totalR1Move += 1
            elif sq == 4:
                totalR2Move += 1

        moveDiff = abs(totalR1Move - totalR2Move)

        if moveDiff > 1:
             raise InvalidEndGameState("Logical error detected! Total moves for each player not adding up")

        return True

    @property
    def CurrentState(self):
        """
        CurrentState getter property for the current game state
        """
        return self.__gameState__

    @property
    def LastMove(self):
        """
        The LastMove getter property for the last move made by a player
        """
        return self.__lastMove__

    @property
    def CurrentGameMsg(self):
        """
        This is a property that is displayed with the rendered grid. It is used to display the
        current gsme state.
        """
        if self.__gameState__ == gameState.Incomplete:
            lastMoveRowCol = self.LastMoveRowColFormat

            msg = """
    Its {} turn!""".format(str(self.turn))

            if self.LastMove.move is not None:
                gameStateMsg = """
    Previous Move by {}
    Last Move Grid Number: {}
    Last Move by Row, column: ({}, {})
    """.format(str(self.LastMove.player), self.LastMove.move, lastMoveRowCol[1], lastMoveRowCol[2])


                msg = msg + gameStateMsg
            return msg

        else:
            return f"Result: {self.__gameState__}"

    @property
    def LastMoveRowColFormat(self):
        """
        After performing a few tests it does make sense when row and col is none for the last
        #move. The only time this makes sense is at the beginning of a game. The game is waiting
        for the initial player to make a move.
        """
        if self.LastMove.move is None:
            return (self.__lastMove__.player, None, None)

        gridNo = self.__lastMove__.move
        row, col = tictactoeGrid.getRowColFromGridNo(gridNo)
        return (self.__lastMove__.player, row, col)

    def __getAvailableMoves__(self):
        if self.__gameState__ != gameState.Incomplete:
            return tuple()

        return tuple(gr for gr in self.grid if self.grid[gr] == 0)

    """
    Double underscores hides the methods and data from documentation. It is the closest
    thing in Python to private methods and attributes however this is convention as there
    is nothing stoping the developer from accessing the hidden methods or attributes if they know
    about it.
    """

    CurrentSymbol = property(__currentSymbol__)
    AvailableMoves = property(__getAvailableMoves__)





"""
This module tests the functionality of the tictactoeGrid class. It uses
unittest.
"""

import unittest
from tictactoe.tictactoeGrid import tictactoeGrid, tictactoeMove
from tictactoe.tictactoeEnums import playerTurn, gameState, gridState, playerSymbol
from tictactoe.tictactoeErrors import gridOccupiedError, InvalidEndGameState
from tictactoe.tictactoeLineCombo import tictactoeLineCombo
from Players.ConsolePlayer import ConsolePlayer
from Players.RandomPlayer import RandomPlayer

def testAndSimulateGame(testcase, moves, turn, endstate):
    """
    This is a function that simulates a game on the tictactoeGrid. This is not
    a test but a function that is called by the unittest testcase instance. After
    each move the gamestate is verified against the expected game state. Until the
    game is completed the end game state will be assumed to be incomplete.

    The function also verifes invalid games for example a player cannot win by more
    than 2 winning lines. A player at most will have made one more move more than the
    opponent if they goes first. Otherwise the moves will be equal if won by the player
    going second. Other game states will be assumed impossible. For example one player
    cannot have made 2 moves more than their opponent.

    Parameters
    ==========
    testcase is an instance of the unittest testcase object.

    moves is an iterable that contains all the moves made by player 1 and player 2
    in order.

    endstate is the expected end game state whether the game is drawn or won by player 1 and
    player 2.

    Raises
    ======
    An InvalidEndGameState is raised if invalid game state is detected.
    """

    t= tictactoeGrid(turn)

    #Everything until the last move should be gameState.Incomplete
    for move in moves[:-1]:
        t.make_move(move)
        testcase.assertEqual(gameState.Incomplete, t.CurrentState)

    #End state will differ depending on test
    t.make_move(moves[-1])
    testcase.assertEqual(t.CurrentState, endstate)

    #Verify that there are no errors in the game state. (optional)
    testcase.assertTrue(t.verifyEndGameIntegrity())

def testLastMovePropAndSimulateGame(testcase, game, turn = playerTurn.Player1):
    """
    This function is called by the unittests to test the LastMove.player and LastMove.move
    property of the tictactoeGrid class. The LastMove represents the last move made by a player.
    LastMove.player is an Enum class that represents the player that made the last
    move. LastMove.move is the getter that represents the move made. The last move
    can be represented in two formats. The first format is row column in which the
    first row is 1 and second row is 2. The last row is 3. The same is for the column
    in which it is represented from 1 to 3. For example row 2 column 2 will represent
    the middle grid. The second format is the grid represented by numbers 1 - 9 as
    illustrated below.

        ==========================
        |   1   |   2   |   3    |
        ==========================
        |   4   |   5   |   6    |
        ==========================
        |   7   |   8   |   9    |
        ==========================

    This test simulates a game and after each move the lastMove property is tested against
    expected values. This is another function called by the test code.

    Parameters
    ==========
    testcase is an instance of the unittest testcase object.

    moves is an iterable that contains all the moves made by player 1 and player 2
    in order.

    turn is an Enum type of playerTurn that represents the player that will go first. If this
    parameter is omitted than the default is that player 1 will go first which is 'O'.

    Raises
    ======
    A error is raised if the expected LastMove getters don't match expected values.
    """

    t = tictactoeGrid(turn)
    """Initial test is to assert that the first expected move is the player but with none values
    because there has not been any moves made yet in a new game.
    """
    initialExpectedMove = tictactoeMove(turn, None)
    testcase.assertEqual(t.LastMove.player, initialExpectedMove.player)
    testcase.assertIsNone(t.LastMove.move)
    testcase.assertTupleEqual(t.LastMoveRowColFormat, (turn, None, None))

    for move, expectedGridFormat, expectedRowColFormat in game:
        t.make_move(move)
        testcase.assertEqual(t.LastMove.player, expectedGridFormat.player)
        testcase.assertEqual(t.LastMove.move, expectedGridFormat.move)
        testcase.assertTupleEqual(t.LastMoveRowColFormat, expectedRowColFormat)

class testTictactoe(unittest.TestCase):
    def testInitGrid(self):
        """
        Method that tests the initial state of the tictactoeGrid grid variable. The grid
        variable should be a dictionary with keys 1 - 9 and values should be all zero.
        """
        tictactoe = tictactoeGrid()
        expected = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        self.assertEqual(tictactoe.grid, expected)

    def testPlayerTurnEnum(self):
        """
        Method tests the expected playerTurn enum value of the tictactoeGrid class. The Enum value should alternate
        between player 1 and player 2 depending on the players turn.
        """
        t = tictactoeGrid()
        self.assertEqual(t.turn, playerTurn.Player1)
        t.make_move(1)
        self.assertEqual(t.turn, playerTurn.Player2)
        t.make_move(2)
        self.assertEqual(t.turn, playerTurn.Player1)

        t.new_game(turn = playerTurn.Player2)
        self.assertEqual(t.turn, playerTurn.Player2)
        t.make_move(1)
        self.assertEqual(t.turn, playerTurn.Player1)

    def testCurrentSymbolProp(self):
        """
        Method that tests the expected values of the tictactoeGrids CurrentSymbol property against
        expected values.
        """
        t = tictactoeGrid()
        symbol = t.CurrentSymbol

        self.assertIsInstance(symbol, playerSymbol)
        self.assertEqual(symbol, playerSymbol.Player1)

        t.make_move(1)
        self.assertEqual(t.CurrentSymbol, playerSymbol.Player2)

    def testRaisesTypeErrorWhenPassingWrongTurnType(self):
        """
        Method tests that a TypeError is raised when any type other than playerTurn Enum is passed to the
        tictactoeGrid initializer.
        """
        with self.assertRaises(TypeError) as ex:
            t = tictactoeGrid(turn = 1)

        #Get the custom error message
        err = ex.exception

        #Exception should include our expected error msg
        self.assertEqual(str(err),"turn should be <enum 'playerTurn'> enum and not <class 'int'>")

    def testMakeMove(self):
        """
        Method that test the expected internal values of tictactoeGrid after the make_move method is called.
        """
        t = tictactoeGrid()
        t.make_move(1)
        expected = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        self.assertEqual(expected, t.grid)
        self.assertTrue(t.turn == playerTurn.Player2)

        t.make_move(5)
        expected = {1: 1, 2: 0, 3: 0, 4: 0, 5: 4, 6: 0, 7: 0, 8: 0, 9: 0}
        self.assertDictEqual(expected, t.grid)
        self.assertTrue(t.turn == playerTurn.Player1)

    def testgridOccupiedError(self):
        """
        Method tests that a gridOccupiedError is raised when a grid is selected as a players move when
        the grid has already been occupied
        """
        t = tictactoeGrid()

        with self.assertRaises(gridOccupiedError) as ex:
            t.make_move(5)
            t.make_move(5)

        self.assertIsInstance(ex.exception, gridOccupiedError)
        #Get the custom error message
        err = ex.exception

        self.assertEqual(str(err),"Grid 5 has already been occupied")

    def testNewGame(self):
        """
        This method tests the internal expected values of tictactoeGrid when the method
        new_game is called.
        """
        t = tictactoeGrid()

        #Simulate game
        t.make_move(4)

        t.new_game()
        expected = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        self.assertDictEqual(expected, t.grid)

    def testItemInIterables(self):
        """
        This function tests the itemsInIterable Function. The itemsInIterables function returns a
        sequence of indexes for which item is contained in a list of sequences.

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

        For example, 1 is contained in WIN_LINES[0], WIN_LINES[3] and WIN_LINES[6] therefore should return
        [0,3,6]

        """
        expected = [(0,[]),(1,[0,3,6]), (2, [0, 4]), (3,[0,5,7]), (4,[1,3]), (5,[1,4,6,7]), (6,[1, 5]),
                   (7,[2,3,7]), (8, [2, 4]), (9, [2, 5, 6])]

        for item, expectedResult in expected:
            actual = tictactoeLineCombo.itemInIterables(item, tictactoeLineCombo.WIN_LINES)
            self.assertEqual(actual, expectedResult, "itemsInIterable test failed")



    def test_getAffectedLines(self):
        expectedDict = {1: [0, 3, 6],
                        2: [0, 4],
                        3: [0, 5, 7],
                        4: [1, 3],
                        5: [1, 4, 6, 7],
                        6: [1, 5],
                        7: [2, 3, 7],
                        8: [2, 4],
                        9: [2, 5, 6]}

        actualDict = tictactoeLineCombo.moveAffectedLines()


        self.assertIsInstance(actualDict, dict, f"A Dictionary is not returned. {type(actualDict)}")
        self.assertEqual(actualDict, expectedDict)

    def testGridState(self):
        """
        This method tests the GridState method against expected values. The GridState function of the
        tictactoeGrid class should accept the grid number as an integer as input and return an Enum type
        of gridState signalling whether a grid is free.
        """
        t = tictactoeGrid()
        t.make_move(1)
        t.make_move(2)

        grid1 = t.gridState(1)
        grid2 = t.gridState(2)
        freeGrid = t.gridState(3)

        self.assertIsInstance(grid1, gridState)
        self.assertIsInstance(grid2, gridState)
        self.assertIsInstance(freeGrid, gridState)

        self.assertEqual(grid1, gridState.Player1)
        self.assertEqual(grid2, gridState.Player2)
        self.assertEqual(freeGrid, gridState.GridFree)

    def testgetGridNoFromRowCol(self):
        """
        Method that tests the getGridNoFromRowCol method of the tictactoeGrid class. The
        diagram below is a aid as the getGridNoFromRowCol accepts row and col as input and
        should return the expected grid number. For example if row is 2 and col is 2 then
        the expected output is 5.

                | col 1 | col 2 | col 3 |
        ===================================
         row 1  |   1   |   2   |   3   |
        ===================================
         row 2  |   4   |   5   |   6   |
        ===================================
         row 3  |   7   |   8   |   9   |
        ===================================

        """

        testData = ((1, 1, 1), (1, 2, 2), (1, 3, 3),
                    (2, 1, 4), (2, 2, 5), (2, 3, 6),
                    (3, 1, 7), (3, 2, 8), (3, 3, 9))

        for row, col, expected in testData:
            self.assertEqual(tictactoeGrid.getGridNoFromRowCol(row, col), expected,
            f"Row: {row} Col: {col} should be {expected}")

    def testgetRowColFromGridNo(self):
        """
        This method tests the getRowColFromGridNo of the tictactoeGrid class.

                | col 1 | col 2 | col 3 |
        ===================================
         row 1  |   1   |   2   |   3   |
        ===================================
         row 2  |   4   |   5   |   6   |
        ===================================
         row 3  |   7   |   8   |   9   |
        ===================================

        The getRowColFromGridNo method accepts the row and column and returns the grid number as output.
        The method is the inverse method of getGridNoFromRowCol. For example if the grid number is 5 then
        the static method should return a tuple of (2, 2) where 2 is row and column number.
        """

        testData = ((1, (1, 1)), (2, (1, 2)), (3, (1, 3))
                    , (4, (2, 1)), (5, (2, 2)), (6, (2, 3))
                    , (7, (3, 1)), (8, (3, 2)), (9, (3, 3)))

        for gridNo, expected in testData:
            self.assertTupleEqual(tictactoeGrid.getRowColFromGridNo(gridNo), expected)

    def testLastMoveProperty(self):
        """
        Method to test LastMove and the LastMoveRowColFormat of the tictactoeGrid class. The difference between the two methods is
        the format of the return value. LastMove returns the move in a grid number format while LastMoveRowColFormat returns a tuple of
        the last move in row and column format. Both methods will also return an enum specifying the player who made the move.

        After refactoring the test code this test method in turn calls testLastMovePropAndSimulateGame to minimise duplicated code. Refer
        to the comments of this method for more details on how the method both these last move properties.

    The following tests were performed.

Keys => Player 1: O or 1
        Player 2: X or 4

        Test 1
        ======
        ==========================
        |   X   |       |   O    |
        ==========================
        |   O   |   O   |        |
        ==========================
        |   X   |  X    |   X    |
        ==========================
        ==========================
        |   4   |   0   |   1    |
        ==========================
        |   1   |   1   |   0    |
        ==========================
        |   4   |   4   |   4    |
        ==========================

    Player 2 to move first.

    Expected in Grid Number format
    ==============================
    expected LastMove property = (player 2) None,(player 2)1,  (player 1)5,  (player 2)9,  (player 1)3,  (player 2)7,  (player 1)4,
    (player 2)8

    Expected in Row Col format
    ==========================
    format is tuple(playerTurn.player, row, col)
    expected LastMove property = (player2, None, None), (player1, 2,  2), (player2, 3, 3), (player1, 1, 3), (player1, 1, 3)
    , (player2, 3, 1), (player1, 2, 1), (player2, 3, 2)

    Test 2
    ======
        ==========================
        |       |   X   |   X    |
        ==========================
        |   X   |   O   |        |
        ==========================
        |   O   |   O   |   O    |
        ==========================
        ==========================
        |   0   |   4   |   4    |
        ==========================
        |   4   |   1   |   0    |
        ==========================
        |   1   |   1   |   1    |
        ==========================
        Player 1 moves first

        Expected in Grid Number format
        ==============================
        moves = (player 1) None ,(player 1) 5,  (player 2) 4,  (player 1) 7,  (player 2)3,  (player 1) 8, (player 2)2,  (player 1)9

        Expected in Row Col format
        ==========================
        moves = (Player 1, None, None), (Player 1, 2, 2), (Player 2, 2, 1), (Player 1, 3, 1), (Player 2, 1, 3), (Player 1, 3, 2)
        , (Player 1, 3, 2), (Player 1, 3, 3)

        Test 3
        ======
        ==========================
        |       |   X   |   X    |
        ==========================
        |   X   |   O   |        |
        ==========================
        |   O   |   O   |   O    |
        ==========================
        ==========================
        |   4   |   0   |   0    |
        ==========================
        |   1   |   4   |   0    |
        ==========================
        |   1   |   0   |   4    |
        ==========================
        Player 1 moves first

        Expected in Grid Number format
        ==============================
        moves = (player 1) None,(player 1)5, (player 2)3,  (player 1)7, (player 2)1,  (player 1)2,  (player 2)8,
        (player 1)4, (player 2)6, (player 1) 9

        Expected in Row Col format
        ==========================
        moves = (player 1, None, None), (player 1,2,2), (player 2,1,3), (player 1,3,1), (player 2,1,1), (player 1,1,2)
        , (player 2,3,2), (player 1,2,1),  (player 2,2,3), (player 1,3,3)
        """

        games = (
                  #Format of tuple is move, expectedMoveGridFormat of type tictactoeMove, expectedMoveRowColFormat of type
                  #tuple(plyer, row, col)
                  (
                    (1, tictactoeMove(playerTurn.Player2, 1), (playerTurn.Player2, 1, 1)),
                    (5, tictactoeMove(playerTurn.Player1, 5), (playerTurn.Player1,2,2)),
                    (9, tictactoeMove(playerTurn.Player2, 9), (playerTurn.Player2,3,3)),
                    (3, tictactoeMove(playerTurn.Player1, 3), (playerTurn.Player1,1,3)),
                    (7, tictactoeMove(playerTurn.Player2, 7), (playerTurn.Player2,3,1)),
                    (4, tictactoeMove(playerTurn.Player1, 4), (playerTurn.Player1,2,1)),
                    (8, tictactoeMove(playerTurn.Player2, 8), (playerTurn.Player2,3,2))
                  ),
                  (
                   (5, tictactoeMove(playerTurn.Player1, 5), (playerTurn.Player1, 2, 2)),
                   (4, tictactoeMove(playerTurn.Player2, 4), (playerTurn.Player2,2,1)),
                   (7, tictactoeMove(playerTurn.Player1, 7), (playerTurn.Player1,3,1)),
                   (3, tictactoeMove(playerTurn.Player2, 3),(playerTurn.Player2,1,3)),
                   (8, tictactoeMove(playerTurn.Player1, 8), (playerTurn.Player1,3,2)),
                   (2, tictactoeMove(playerTurn.Player2, 2), (playerTurn.Player2, 1, 2)),
                   (9, tictactoeMove(playerTurn.Player1, 9), (playerTurn.Player1,3,3))
                  ),
                  (
                   (5, tictactoeMove(playerTurn.Player1, 5), (playerTurn.Player1, 2, 2)),
                   (3, tictactoeMove(playerTurn.Player2, 3),(playerTurn.Player2,1,3)),
                   (7, tictactoeMove(playerTurn.Player1, 7), (playerTurn.Player1,3,1)),
                   (1, tictactoeMove(playerTurn.Player2, 1), (playerTurn.Player2, 1, 1)),
                   (2, tictactoeMove(playerTurn.Player1, 2), (playerTurn.Player1, 1, 2)),
                   (8, tictactoeMove(playerTurn.Player2, 8), (playerTurn.Player2,3,2)),
                   (4, tictactoeMove(playerTurn.Player1, 4), (playerTurn.Player1,2,1)),
                   (6, tictactoeMove(playerTurn.Player2, 6), (playerTurn.Player2, 2, 3)),
                   (9, tictactoeMove(playerTurn.Player1, 9), (playerTurn.Player1,3,3))
                  )
                )

        # testLastMovePropAndSimulateGame(testcase, game, turn = playerTurn.Player1)
        for game in games:
            testLastMovePropAndSimulateGame(self, game, game[0][1].player)



    def testValidGameState(self):
        """
        Test for validating game state whether the game is won by player 1, 2 or draw or even
        incomplete. Before the algorithm checks for winning lines for all lines after every
        move. I didn't like this. I have changed it so that winning lines that can be won by the players
        move is checked. Meaning we check the minimal lines required depending on the move.
        For example if a player selects the middle grid than there are four possibilities
        of a winning combo. A counter is used to keep track of the number of moves and the combo
        lines are checked after the miminum moves have been met to win a game. It is possible to win
        a game in 5 moves (This is inclusive of both players moves added together).

        There is an OPTIONAL method called verifyEndGameIntegrity that can be called at the end of the
        game to check for end game integrity. This method isn't absolutely required but I kept it for debugging
        purposes.
        """
        """
        The following tests were performed

        Test 1
        ======

        Player 1 = O or 1 (sum of 3 for player 1 win)
        Player 2 = X or 4 (sum of 12 for player 2 win)

        ==========================
        |   X   |       |   O    |
        ==========================
        |   O   |   O   |        |
        ==========================
        |   X   |   X    |   X   |
        ==========================
        ==========================
        |   4   |   0   |   1    |
        ==========================
        |   1   |   1   |   0    |
        ==========================
        |   4   |   4   |   4    |
        ==========================

        moves = 1, 5, 9, 3, 7, 4, 8
        Player 2 moves first
        Player 2 wins

        Test 2
        ======

        Player 1 = O or 1 (sum of 3 for player 1 win)
        Player 2 = X or 4 (sum of 12 for player 2 win)
        ==========================
        |       |   X   |   X    |
        ==========================
        |   X   |   O   |        |
        ==========================
        |   O   |   O   |   O    |
        ==========================
        ==========================
        |   0   |   4   |   4    |
        ==========================
        |   4   |   1   |   0    |
        ==========================
        |   1   |   1   |   1    |
        ==========================
        moves = 5, 4, 7, 3, 8, 2, 9
        Player 1 moves first
        Player 1 wins

        Test 3
        ======

        Player 1 = O or 1 (sum of 3 for player 1 win)
        Player 2 = X or 4 (sum of 12 for player 2 win)

        ==========================
        |       |   X   |   X    |
        ==========================
        |   X   |   O   |        |
        ==========================
        |   O   |   O   |   O    |
        ==========================
        ==========================
        |   4   |   0   |   0    |
        ==========================
        |   1   |   4   |   0    |
        ==========================
        |   1   |   0   |   4    |
        ==========================
        moves = 5, 4, 9, 7, 1
        Player 2 moves first
        Player 2 wins

        Test 4
        ======

        Player 1 = O or 1 (sum of 3 for player 1 win)
        Player 2 = X or 4 (sum of 12 for player 2 win)

        ==========================
        |       |   X   |   X    |
        ==========================
        |   X   |   O   |        |
        ==========================
        |   O   |   O   |   O    |
        ==========================
        ==========================
        |   4   |   0   |   0    |
        ==========================
        |   1   |   4   |   0    |
        ==========================
        |   1   |   0   |   4    |
        ==========================
        moves = 5, 3, 7, 1, 2, 8, 4, 6, 9
        Player 1 moves first
        Draw
        """
        games = (((1, 5, 9, 3, 7, 4, 8), gameState.Player2Win, playerTurn.Player2)
                ,((5, 4, 7, 3, 8, 2, 9), gameState.Player1Win, playerTurn.Player1)
                ,((5, 4, 9, 7, 1), gameState.Player2Win, playerTurn.Player2)
                ,((5, 3, 7, 1, 2, 8, 4, 6, 9), gameState.Draw, playerTurn.Player1))

        expectedResult = (gameState.Player2Win, gameState.Player1Win, gameState.Player2Win, gameState.Draw)

        turn = (playerTurn.Player2, playerTurn.Player1, playerTurn.Player2, playerTurn.Player1)

        for move, expectedResult, turn in games:
            testAndSimulateGame(self, move, turn, expectedResult)

    def testInvalidGameState(self):
        """
        This function tests the verifyEndGameIntegrity() function of the tictactoeGrid class which raises
        an InvalidEndGameState error when it detects an invalid game by manually checking for logical errors.
        The verifyEndGameIntegrity() function isn't really needed but I have used in when developing this basic
        app to catch logical errors and see no reason not to include it.

        Usually the players calls the make_move() method of the tictactoeGrid class to play the tictactoe game. However
        we are going to cheat here and directly assign the values to the necessary data members of the tictactoeGrid class
        especially those with underscores. Variables with underscores are internal variables and shouldn't be accessed however
        this at most is just a convention and there is nothing stopping you from doing it. What we doing to similar to spoofing
        data packets in a network conversation, playing about with network integrity. In this instance we're playing about with
        the game integrity.

        Test 1
        ======
        ==========================
        |   X   |   X   |   O    |
        ==========================
        |   O   |   O   |   O    |
        ==========================
        |   O   |   X   |   X    |
        ==========================
        ==========================
        |   4   |   4   |   1    |
        ==========================
        |   1   |   1   |   1    |
        ==========================
        |   1   |   4   |   4    |
        ==========================

        Game is set to draw when clearly player 1 wins

        Test 2
        ======
        ==========================
        |   X   |   O   |        |
        ==========================
        |   X   |   O   |        |
        ==========================
        |   X   |   O   |        |
        ==========================
        ==========================
        |   4   |   1   |   0    |
        ==========================
        |   4   |   1   |   0    |
        ==========================
        |   4   |   1   |   0    |
        ==========================

        Game is set to draw when clearly player 1 wins

        Test 3
        ======
        ==========================
        |       |       |        |
        ==========================
        |   X   |   O   |        |
        ==========================
        |   X   |   O   |        |
        ==========================
        ==========================
        |   0   |   0   |   0    |
        ==========================
        |   4   |   1   |   0    |
        ==========================
        |   4   |   1   |   0    |
        ==========================

        Game is set to draw when clearly the game is incomplete

        Test 4
        ======
        ==========================
        |   X   |   X   |    X   |
        ==========================
        |   X   |   X   |    X   |
        ==========================
        |   X   |   X   |    X   |
        ==========================
        ==========================
        |   4   |   4   |   4    |
        ==========================
        |   4   |   4   |   4    |
        ==========================
        |   4   |   4   |   4    |
        ==========================

        Game is set to Player 2 win but a game like this is clearly impossible

        Test 5
        ======
        ==========================
        |   X   |   X   |    X   |
        ==========================
        |   X   |   X   |    O   |
        ==========================
        |   X   |   O   |    X   |
        ==========================
        ==========================
        |   4   |   4   |   4    |
        ==========================
        |   4   |   4   |   1    |
        ==========================
        |   4   |   1   |   4    |
        ==========================

        Game is set to Player 2 win but a game like this is clearly impossible

        Test 6
        ======
        ==========================
        |   O   |       |        |
        ==========================
        |       |       |        |
        ==========================
        |       |       |        |
        ==========================
        ==========================
        |   1   |   0   |   0    |
        ==========================
        |   0   |   0   |   0    |
        ==========================
        |   0   |   0   |   0    |
        ==========================

        In this last test we call verifyEndGameIntegrity() when clearly the game
        has no result at the moment and still incomplete. This differs from the other tests
        because we do not have to mess around with the integrity of the game.

        """
        games = (({1:4, 2:4, 3:1, 4:1, 5:1, 6:1, 7:1, 8:4, 9:4}, 9, gameState.Draw)
                ,({1:4, 2:1, 3:0, 4:4, 5:1, 6:0, 7:4, 8:1, 9:0}, 6, gameState.Player1Win)
                ,({1:0, 2:0, 3:0, 4:4, 5:1, 6:0, 7:4, 8:1, 9:0}, 4, gameState.Draw)
                ,({1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4}, 9, gameState.Player2Win)
                ,({1:4, 2:4, 3:4, 4:4, 5:4, 6:1, 7:4, 8:1, 9:4}, 9, gameState.Player2Win))

        t = tictactoeGrid()

        """attributes with underscores are read only attributes and internal. You shouldn't assign values to them
           however this is an exception as we are simulating and testing for logical errors in which verifyEndGameIntegrity
           will throw an InvalidEndGameState error. Attributes with underscores is Pythons method of signalling
           that the data member is private and internal however this is only convention and there is nothing stopping
           you from accessing and assigning values to the variable
        """
        for t.__grid__, t.__totalMoves__ , t.__gameState__ in games:
            with self.assertRaises(InvalidEndGameState):
                t.verifyEndGameIntegrity()

        #Simulate incomplete game by making one move
        t.new_game()
        t.make_move(1)

        with self.assertRaises(InvalidEndGameState):
            t.verifyEndGameIntegrity()

    def testPropsAreReadOnly(self):
        """
        This method tests the getters of the following properties: grid,
        CurrentState, CurrentSymbol, LastMove, AvailableMoves, and LastMoveRowColFormat.
        Some of these getters are methods that are decorated with property decorator
        such as the CurrentState property. Other properties such as CurrentSymbol is
        done through the property method and have equivalent internal variable counterparts
        such as __currentSymbol__. You should access these properties through the getters and
        you should not change the internal counterparts which is why getters are provided. It
        is there to provide readonly access to the data. Howvever in Python these are only
        conventions and can be accessed at your own risk.

        This method tests that the getters are accessible in the tictactoe class. It also tests
        that an AttributeError is raised when attempting to assign a value to the getter property.
        """
        t = tictactoeGrid()


        objAttributes = ("grid", "CurrentState","CurrentSymbol","LastMove"
                        ,"AvailableMoves", "LastMoveRowColFormat")

        #Test for existence of attribute
        for attribute in objAttributes:
            self.assertTrue(hasattr(t, attribute))

        """
        With read only attributes we should get an AttributeError when trying
        to assign a value to the attribute. We can read from the property but we
        cannot assign values to it. Properties are generally getters and setters.
        We defined the getter and we purposely didn't define the setter making property
        read only.
        """
        with self.assertRaises(AttributeError):
            t.grid = None

        with self.assertRaises(AttributeError):
            t.CurrentState = gameState.Draw

        with self.assertRaises(AttributeError):
            t.CurrentSymbol = playerSymbol.Plager1

        with self.assertRaises(AttributeError):
            t.LastMove = tictactoeMove(playerTurn.Player1, 1)

        with self.assertRaises(AttributeError):
            t.AvailableMoves = ()

        with self.assertRaises(AttributeError):
            t.LastMoveRowColFormat = (playerTurn.Player1, 2, 2)

    def testGetAvailableMoves(self):
        """
        This method tests the AvailableMoves property of the tictactoeGrid
        object against expected values.
        """
        t = tictactoeGrid()
        t.make_move(2)
        t.make_move(4)

        self.assertTupleEqual(t.AvailableMoves, (1, 3, 5, 6, 7, 8, 9))

        t.make_move(6)
        self.assertTupleEqual(t.AvailableMoves, (1,3,5,7,8,9))

        t.make_move(3)
        self.assertTupleEqual(t.AvailableMoves, (1,5,7,8,9))

        moves =(5, 3, 7, 1, 2, 8, 4, 6, 9)
        t.new_game()

        #Simulate draw game
        for move in moves:
            t.make_move(move)

        self.assertTupleEqual(t.AvailableMoves, ())

    def testRenderGrid(self):
        """
        This method tests the renderedGrid property of the tictactoeGrid
        class against expected values. renderedGrid is a multiline string
        property that represents the tictactoe grid. It is updated after
        every move.
        """

        t = tictactoeGrid()

        expected = """
    =============================
    |         |         |        |
    =============================
    |         |         |        |
    =============================
    |         |         |        |
    ============================="""

        self.assertTrue(expected in t.renderedGrid)

        expectedMsg = "Its Player 1 turn!"

        self.assertTrue(expectedMsg in t.renderedGrid)

        moves = (5, 4, 7, 3, 8, 2)

        for move in moves:
            t.make_move(move)

        expected = """
    =============================
    |         |    X    |    X   |
    =============================
    |    X    |    O    |        |
    =============================
    |    O    |    O    |        |
    ============================="""

        self.assertTrue(expected in t.renderedGrid)
        self.assertTrue("Its Player 1 turn" in t.renderedGrid)
        self.assertTrue("Previous Move by Player 2" in t.renderedGrid)
        self.assertTrue("Last Move Grid Number: 2" in t.renderedGrid)
        self.assertTrue("Last Move by Row, column: (1, 2)" in t.renderedGrid)

        t.make_move(9)

        expected = """
    =============================
    |         |    X    |    X   |
    =============================
    |    X    |    O    |        |
    =============================
    |    O    |    O    |    O   |
    ============================="""

        self.assertTrue(expected in t.renderedGrid)
        self.assertTrue("Result: Player 1 Win" in t.renderedGrid)

        t.new_game(turn=playerTurn.Player1)

        moves = (5, 3, 7, 1, 2, 8, 4, 6, 9)

        for move in moves:
            t.make_move(move)

        expected = """
    =============================
    |    X    |    O    |    X   |
    =============================
    |    O    |    O    |    X   |
    =============================
    |    O    |    X    |    O   |
    ============================="""

        self.assertTrue(expected in t.renderedGrid)
        self.assertTrue("Result: Draw" in t.renderedGrid)

    def testGameAlreadyCompletedError(self):
        """
        Function tests that a gameAlreadyCompletedError is raised when a player attempts a
        move after a game has already ended. It also verifies that the property AvailableMoves
        returns an empty tuple signalling that there are no available moves in game when it has ended.

        The following test is performed.

        ==========================
        |       |   X   |   X    |
        ==========================
        |   X   |   O   |        |
        ==========================
        |   O   |   O   |   O    |
        ==========================
        ==========================
        |   0   |   4   |   4    |
        ==========================
        |   4   |   1   |   0    |
        ==========================
        |   1   |   1   |   1    |
        ==========================
        moves = 5, 4, 7, 3, 8, 2, 9
        """
        moves = (5, 4, 7, 3, 8, 2, 9)
        grid = tictactoeGrid()

        for move in moves:
            grid.make_move(move)

        self.assertEqual(grid.CurrentState, gameState.Player1Win)
        self.assertTupleEqual(grid.AvailableMoves, tuple())




if __name__ == '__main__':
    unittest.main()
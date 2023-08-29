"""
This module tests the functionality of all the classes that inherit from tictactoePlayer which is the ConsolePlayer and RandomPlayer
class.

I tend to keep my tests very simple and avoid using mock objects whenever possible. Mock objects are replacement objects and methods
that replaces and patch method and objects dynamically. ConsolePlayer is a class that represents a tictactoe player using
the console. So, the user will enter their moves interacting with the console. I only use the input() function to get
user input for the ConsolePlayer.

How do you test for console input? You can use mock objects and patch the input function. This means when the test code is
executed and encounters the input function it is replaced dynamically with our mock object (function). In most cases the
mock object is just a function or object that replaces the original input function. Luckily unittests has support for mock objects.
We only need to use the patch decorator which is very easy to understand.
"""

from Players.RandomPlayer import RandomPlayer
from Players.ConsolePlayer import ConsolePlayer, withinRange
from Players.tictactoePlayer import tictactoePlayer, NotMyTurnError
import unittest
from tictactoe.tictactoeGrid import tictactoeGrid
from tictactoe.tictactoeEnums import playerTurn, gameState
from tictactoe.tictactoeErrors import gridOccupiedError
from unittest.mock import patch


class WorldDumbestPlayer(tictactoePlayer):
    """
    This class was created to test that a gridOccupiedError is raised when
    selecting an occupied grid as the selected move. A test class is required
    as our main player classes will never select a move that isn't available
    because the available moves are stored in a iterable and this iterable is
    updated after every move. This class only knows to select grid 1 as their move.
    So it is always going to raise an error at some point in the game.

    We could alternatively just use a mock object.
    """
    def __init__(self, board, turn):
        super().__init__(board, turn)

    #This player will keep selecting 1 as their move triggering an error
    def getMove(self):
        return 1

class testingClassOnly(tictactoePlayer):
    """
    This is another class created for testing. This player will always select
    the first available grid.
    """
    def __init__(self, board, turn):
        super().__init__(board, turn)

    #This class will select the first available grid
    def getMove(self):
        return self.board.AvailableMoves[0]

class testPlayers(unittest.TestCase):
    """
    This class tests the functionality of all the classes that inherit from tictactoePlayer which is
    the ConsolePlayer and RandomPlayer class.
    """
    def testInheritance(self):
        """
        This tests that the RandomPlayer class and the ConsolePlayer class do inherit from tictactoePlayer and
        that both classes contain the getMove method.
        """
        self.assertTrue(ConsolePlayer, "getMove")
        self.assertTrue(RandomPlayer, "getMove")
        self.assertTrue(issubclass(RandomPlayer, tictactoePlayer))
        self.assertTrue(issubclass(ConsolePlayer, tictactoePlayer))

    def testRaisesNotMyTurnError(self):
        """
        Function test that a NotMyTurnError is raised when placing a move when it is not your turn.
        """
        impatientPlayer = RandomPlayer(tictactoeGrid(turn=playerTurn.Player2), playerTurn.Player1)
        with self.assertRaises(NotMyTurnError) as ex:
            impatientPlayer.placeMove()

            #I like the error message. Assert that it prints the error message
        self.assertEqual(str(ex.exception), "Please be patient and wait for your turn before placing your move")

    def testRandomGetMove(self):
        """
        This methods tests the LastMove property of the RandomPlayer class against expected values.
        It also verifies the length of the AvailableMoves list property against expected lengths.
        """
        grid = tictactoeGrid(turn=playerTurn.Player1)
        testObj = testingClassOnly(grid, playerTurn.Player2)
        r = RandomPlayer(grid, turn=playerTurn.Player1)
        r.placeMove()

        #List indexes start from 0
        self.assertTrue(grid.LastMove.move >= 1 and grid.LastMove.move <= 9)
        testObj.placeMove()
        r.placeMove()

        self.assertTrue(grid.LastMove.move >= 1 and grid.LastMove.move <= 9)

        #Two moves have been made. Length of list of AvailableMoves is 6
        self.assertTrue(len(grid.AvailableMoves) == 6)

        count = 0
        for x in range(1, 10):
            if grid.grid[x] > 0:
                count += 1

        self.assertEqual(count, 3)

    def testTwoMostDumbestPlayersEver(self):
        """Test Random Player v Random Player. Simple test to create two random players to
           play against each other 1000 times. There should be a result after each game meaning the
           game will end up with a win or a draw. We will then verify game integrity after each game,
           checking for logical errors. Also we will have two separate counters to keep track of the
           number of moves each random players makes. There should either be roughly equal or at most one
           player has made one more move then the other. In either case the grid should have same number of
           1's and 4's in the Dictionary. THIS WILL BE FUN. LETS PLAY."""

        grid = tictactoeGrid()
        r1 = RandomPlayer(grid, playerTurn.Player1)
        r2 = RandomPlayer(grid, playerTurn.Player2)

        #For our test to work the grid reference has be to passed to r1 and r2's init method by REFERENCE.
        #For players to play against
        #each other they must be playing on the same grid.
        #Objects are usually passed something similar to reference cos passing by value will be too much work ie Lists and
        #large objects.
        #I read that Python passes the objects reference by value (whatever that means) so we can test this using id().

        self.assertEqual(id(r1.board), id(r2.board))
        self.assertEqual(id(grid), id(r1.board))

        for i in range(1000):
            r1MoveCount = 0
            r2MoveCount = 0

            #For simplicity r1 will always go first
            grid.new_game(turn=playerTurn.Player1)

            while(grid.CurrentState == gameState.Incomplete):
                r1.placeMove()
                r1MoveCount += 1

                if(grid.CurrentState != gameState.Incomplete):
                    break

                r2.placeMove()
                r2MoveCount += 1

            #Check for logical errors and end game integrity. An InvalidEndGameState error will be raised
            #if logical error detected.
            self.assertTrue(grid.verifyEndGameIntegrity())

            #There has to be a result other than incomplete
            self.assertTrue(grid.CurrentState.value >= 1 and grid.CurrentState.value <= 3)

    def testgridOccupiedError(self):
        """
        This method tests that a gridOccupiedError is raised when a player selects a move that has already
        been occupied.
        """

        grid = tictactoeGrid()
        dumbPlayer = WorldDumbestPlayer(grid, playerTurn.Player1)
        randPlayer = RandomPlayer(grid, playerTurn.Player2)

        dumbPlayer.placeMove()
        randPlayer.placeMove()

        with self.assertRaises(gridOccupiedError):
            dumbPlayer.placeMove()

    def testWithinRange(self):
        """
        This method will test the return values of the withinRange function
        against expected values
        """
        self.assertTrue(withinRange(5, 10, 5))
        self.assertTrue(withinRange(5, 10, 10))
        self.assertFalse(withinRange(5,10,11))
        self.assertFalse(withinRange(5,10,4))


    def testConsolePlayerparseAndValidateMove(self):
        """
        Because I refactored the code so that a validation method validates console input we can test the
        validation code with minimal mock objects. Infact the only method we need to patch is the input()
        function. However this function doesn't require any patching because we are just testing that the
        code validates invalid input. We pass the input as a string so we can just test the static method
        called
        """

        #We assume grid 5, 7, 8, 9 have been taken
        available = (1, 2, 3, 4, 6)

        #Testing can become a tedious task meaning we should aim for 100% code coverage. What does this mean?
        #It means we need to test all logic, conditions, functions and inputs within our code. Easy said then done
        testdata = (("rubbish", "Error! Its row and column separated by spaces. Try again!"),
                    ("row1 1", "Rows and column must be in numeric format try again!"),
                    ("1", "Error! Its row and column separated by spaces. Try again!"),
                    ("0 3", "Row and column has to be with the range of 1-3. Try again!"),
                    ("3 0", "Row and column has to be with the range of 1-3. Try again!"),
                    (None, "Unexpected error!"))

        for invalidInput, expectedErrorMsg in testdata:
            gridNo, actualMsg = ConsolePlayer.parseAndValidateMove(invalidInput, available)
            #When we cannot parse row and column None is returned
            self.assertIsNone(gridNo)
            self.assertEqual(actualMsg, expectedErrorMsg)

        #Test that method invalidates a selected move that has already been taken. For that we neeed to convert
        #row and column to grid number. row 3 and column 3 is grid 9.

        gridno = tictactoeGrid.getGridNoFromRowCol(3, 3)

        self.assertEqual(gridno, 9)

        gridno, errorMsg = ConsolePlayer.parseAndValidateMove("3 3", available)

        self.assertIsNone(gridno)
        self.assertEqual(errorMsg, "This grid has already been occupied. Please try again!")

    """
    The first time we have to use a mock object to patch the input method. Everytime
    it encounters input it uses the mockinput argument to just return the values in side_effect
    in the order the list items are declared. This method just checks that the console input is parsed properly.
    """
    @patch('builtins.input', side_effect=['2 2', '3 1', '3 2'])
    def testConsolePlayerPlaceMoveConsoleInput(self, mockinput):
        """

        The following tests were used

        Test
        ====

        ==========================
        |       |   X   |        |
        ==========================
        |   X   |   O   |        |
        ==========================
        |   O   |   O   |        |
        ==========================

        move = (p1) 5, (p2) 2, (p1) 7, (p2) 4, (p1) 8

        ==========================
        |   0   |   4   |   0    |
        ==========================
        |   4   |   1   |   0    |
        ==========================
        |   1   |   1   |   0    |
        ==========================

        expected dictionary = {1:0, 2:4, 3:0,
                               4:4, 5:1, 6:0,
                               7:1, 8:1, 9:0}
        """

        grid = tictactoeGrid(playerTurn.Player1)
        player = ConsolePlayer(grid, playerTurn.Player1)

        player.placeMove()
        for move in (2, 4):
            grid.make_move(move)
            player.placeMove()

        expected = {1:0, 2:4, 3:0,
                    4:4, 5:1, 6:0,
                    7:1, 8:1, 9:0}

        self.assertDictEqual(player.board.grid, expected)
        self.assertDictEqual(player.board.grid, grid.grid)

    @patch('builtins.input', side_effect=['2 2','rubbish','4 4','3 1', '3 2'])
    def testConsolePlayerGetMoveParsesCorrectGridNo(self, mockinput):
        """
        Method tests that GetMove method of the player classes against expected values.
        """
        grid = tictactoeGrid(playerTurn.Player1)
        player = ConsolePlayer(grid, playerTurn.Player1)

        #row 2 col 2 is grid 5
        self.assertEqual(player.getMove(), 5)

        #The getMove() keeps prompting for input if its invalid. We will test
        #that we are not stuck in an infinite loop and we eventually get the
        #grid no when the input is valid

        #First two input are invalid - rubbish, 4 4 (out of range)
        #Next input is valid - 3 1
        self.assertEqual(player.getMove(), 7)

        self.assertEqual(player.getMove(), 8)

        #Were we really reprompted when the input was invalid. We can verify this
        #by looking at the call count. We patched 3 valid inputs and 2 invalid inputs so
        #we would have been prompted 5 times
        assert mockinput.call_count == 5

if __name__ == '__main__':
    unittest.main()
"""
This module contains all the unit tests that tests the functionality of the tictactoeFactory class
"""

import unittest
from unittest.mock import patch
from tictactoeFactory import TictactoeGameBuilder, tictactoeFromConsoleBuilder
from tictactoeEnums import playerType, playerTurn
from ConsolePlayer import ConsolePlayer
from RandomPlayer import RandomPlayer
from tictactoeGrid import tictactoeGrid


class test_tictactoeFactory(unittest.TestCase):
    def testInheritance(self):
        """
        This method tests that the tictactoeFromConsoleBuilder is a subclass of the
        TictactoeGameBuilder class and it inherits the createGame from the TictactoeGameBuilder
        class
        """
        self.assertTrue(issubclass(tictactoeFromConsoleBuilder, TictactoeGameBuilder))
        self.assertTrue(hasattr(TictactoeGameBuilder, "createGame"))
        self.assertTrue(hasattr(tictactoeFromConsoleBuilder, "createGame"))

    def test_validateSymbol__(self):
        """
        This method tests the functionality of the static __validateSymbol__ method against expected values.
        __validateSymbol__ validates the players console input when selecting their chosen symbol.
        """
        testData = (("0",  "Try again. Symbols can only be O or X"),
                    ("rubbish",  "Try again. Symbols can only be O or X"),
                    (None, "Unexpected error!"))

        for invalidInput, expectedMsg in testData:
            success, actualMsg = tictactoeFromConsoleBuilder.__validateSymbol__(invalidInput)
            self.assertFalse(success)
            self.assertEqual(actualMsg, expectedMsg)

        validInputTestData = (("O",  "You got it. you are O"),
                              ("X", "You got it. you are X"),
                              (" O","You got it. you are O"),
                              ("x", "You got it. you are X"))

        for validInput, expectedMsg in validInputTestData:
            success, actualMsg = tictactoeFromConsoleBuilder.__validateSymbol__(validInput)
            self.assertTrue(success)
            self.assertEqual(actualMsg, expectedMsg)

    def test__validatePlayerInput__(self):
        """
        This method tests the __validatePlayerInput__ static function of the tictactoeFromConsoleBuilder class
        against expected values.
        """

        testData = (("1", True, playerType.Random, "You will be playing against a Random Player"),
                    ("2", True, playerType.Console, "You will be playing against a Console Player"),
                    (" 2", True, playerType.Console, "You will be playing against a Console Player"),
                    (None, False, None, "Unexpected error!"),
                    ("O", False, None, "Error! Enter 1 for Random Player or 2 for Console Player. Try again!"))

        for userInput, expectedSuccess, player, expectedMsg in testData:
            actualSuccess, actualPlayer, actualMsg = tictactoeFromConsoleBuilder.__validatePlayerInput__(userInput)
            self.assertEqual(actualSuccess, expectedSuccess)
            self.assertEqual(actualPlayer, player)
            self.assertEqual(actualMsg, expectedMsg)

    def test_validateTurn(self):

        testData = (("Y", True, True, "OK you go first"),
                    ("N", True, True, "OK you go second"),
                    ("y", True, True, "OK you go first"),
                    (" y", True, True, "OK you go first"),
                    ("rubbish", False, None, "Please enter Y or N. Try again!"),
                    (None, False, None, "Unexpected error!"))

        for userInput, expectedSuccess, expectedP1goFirst, expectedMsg in testData:
            actualSuccess, actualP1goFirst, actualMsg = tictactoeFromConsoleBuilder.__validateTurn__(userInput)


    """
    __getPlayerSelection__() of the tictactoeFromConsoleBuilder class is a static method that keeps prompting the user
    for the type of symbol they wish to have. 'O' or 'X'.
    1) User enters 'O' for 'O'
    2) User enters 'X' for 'X'

    This is where we start patching the input() function. However this is very quick now because the method for validating invalid
    user input has already been tested. The input string is simply passed to the validation function. So, all we are doing is confirming
    that we get the correct player enum from the return value and we are reprompted for the player type if the input is anything but 1, and
    2. We can simply look at the call count of the mock input function. Its as simple as that otherwise if there are errors we potentially
    can get stuck in an infinite loop.
    """

    @patch('builtins.input', side_effect=['O','rubbish','0', 'more rubbish', ' X'])
    def test__getPlayerSelection__(self, mockinput):
        """
        Method that tests that the __getPlayerSelection__ method keeps prompting the user for input until the input is valid.
        We can easily confirm this by passing in invalid inputs to the __getPlayerSelection__ function followed by a valid input.
        We can then examine the number of times the input function was patched against expected values.
        """

        #This static method keeps prompting for input until the the user input is valid.
        #Valid inputs are listed below.
        #Player 1 for O
        #Player 2 for X
        actualEnum = tictactoeFromConsoleBuilder.__getPlayerSelection__()

        self.assertEqual(actualEnum, playerTurn.Player1)

        actualEnum = tictactoeFromConsoleBuilder.__getPlayerSelection__()

        self.assertEqual(actualEnum, playerTurn.Player2)

        #The total times the patch input function was called is 5 times. We entered 2 valid values
        #but was reprompted 3 times since the middle values were not valid.
        assert mockinput.call_count == 5


    @patch('builtins.input', side_effect=['Y','rubbush','0', 'more rubbish', 'N'])
    def test__getTurnFromConsole__(self, mockinput):
    
            """
            Method tests the __getTurnFromConsole__ static method of the tictactoeFromConsoleBuilder class reprompts for console input when 
            user inputs invalid values. Again we will test this against the number of times the input function was patched. The more
            invalid values we enter the more times the input function is patched.
           
            Users enter y if they wish to go first or n if they wish to go second. All other input will be invalid. An enum of true is returned if
            you go first or otherwise false.
            """

        #Here we are only prompted once because the first input is Y which is valid
        self.assertTrue(tictactoeFromConsoleBuilder.__getTurnFromConsole__())

        #Here we are only prompted 4 times because the next set of inputs consists of 3 invalid inputs
        #before a valid input is entered (or mocked to be more accurate)
        #Return value should be false because we don't expect to go first
        self.assertFalse(tictactoeFromConsoleBuilder.__getTurnFromConsole__())

        assert mockinput.call_count == 5


    @patch('builtins.input', side_effect=['1','rubbush','0', 'more rubbish', ' 2'])
    def test__getPlayerType__(self, mockinput):
        """
        Method tests the functionality of the __getPlayerType__ static method of the 
        tictactoeFromConsoleBuilder class. Because the user inputs the choice for the 
        type of player they wish to play against. We will test the number of times the 
        patch input function was called to confirm that we were reprompted. An enum of 
        playerType is returned representing the type of player requested.

        Users enter 1 to play against a Random Player
        Users enter 2 to play against a Console Player
        """

        #We are only prompted once here
        self.assertEqual(tictactoeFromConsoleBuilder.__getPlayerType__(), playerType.Random)

        #We are prompted 4 times on this call as the initial 3 values are invalid
        self.assertEqual(tictactoeFromConsoleBuilder.__getPlayerType__(), playerType.Console)

        #input should be patched a total of 5 times and we should not be stuck in some infinite loop because
        #eventually we do enter valid values

        assert mockinput.call_count == 5

    """
    This method tests the __fromConsole__ static method of the tictactoeFromConsoleBuilder class. All __fromConsole__ does is return
    a tuple of all the necessary arguments to create the tictactoe game. it prompts the arguments from the user console input. In other
    words it calls all the console input methods we just mentioned. We have already broken the code into more distinct methods so we can
    just test for the expected return values. Note leading spaces are trimmed and input is case insensitive.

    The order in which the user is prompted is
    1) User is firstly prompted for symbol - Valid inputs are
    O for O
    X for X

    2) User is then prompted for whether they wish to go first. Valid inputs are
    Y to go first
    N to go second

    3) Finally user is prompted on the type of player they wish to play against
    1 for Random Player
    2 for Console Player

    Player 1 is the user and will always be console player however the createGame method of the
    tictactoeFromConsoleBuilder class will allow you to create two Random Players if you want so
    you could easily modify the program to allow you dumb random players playing tictactoe at speed with
    abolutely no intelligence.

    Note only player 1 configuration is returned in the tuple. Because player 2 configuration relies on player 1.

    i.e. If player 1 is 'O' then player 2 is 'X'
    i.e. If player 1 goes first then player 2 must go second.
    Player 1 will always be console player and they choose their opponent type.

    Also note playerTurn.Player1 is 'O'. If you wish to be 'X' then you need to be playerTurn.Player2
    """

                                         #Player 1 to be O, go first and play against Random player
    @patch('builtins.input', side_effect=['O', 'Y', '1'
                                         #Player 1 to be X, go second and play against Console player
                                          ,'X', 'N', '2'
                                         #Player 1 to be O, go second and play against Random player
                                          ,'O', 'N', '1'
                                        #Player 1 to be X, go first and play against Console player
                                          ,'X', 'Y', '2'])

    def test__fromConsole__(self, mockinput):
    
        """
        This method tests the functionality of the __fromConsole__ method of the tictactoeFromConsoleBuilder class.
        All inputs in this function are valid. We are not testing for call count in this test. We are testing
        the return values against expected values.
        """

        #playerTurn.Player1 is 'O'. If you  wish to 'X' then you need to select playerTurn.Player2.
        #Either player can go first regardless of the symbol.
        #Player 1 will always be console and is hardcoded.
        #Format of tuple (player, goFirst, player2Type)
        expectedValues = ((playerTurn.Player1, True, playerType.Random),
                    (playerTurn.Player2, False, playerType.Console),
                    (playerTurn.Player1, False, playerType.Random),
                    (playerTurn.Player2, True, playerType.Console))

        for expected in expectedValues:
            self.assertSequenceEqual(expected, tictactoeFromConsoleBuilder.__fromConsole__())


        assert mockinput.call_count == 12

                                         #Player 1 to be O, go first and play against Random player
    @patch('builtins.input', side_effect=['O',"InvalidArg1",'Y',"InvalidArg2",'1'
                                         #Player 1 to be X, go second and play against Console player
                                          ,'X','3','N', '2'
                                         #Player 1 to be O, go second and play against Random player
                                          ,'5','O', 'N', '1'
                                        #Player 1 to be X, go first and play against Console player
                                          ,'xxxX','X', 'Y', '0','2'])
    def test__fromConsole__withInvalidArgs(self, mockinput):
    
        """
        This test method is very similar to test__fromConsole__ however it includes invalid inputs. Recall 
        that you are reprompted if the input is invalid. We can test that we were reprompted by looking at 
        the call count of the mockinput object.

        The test data is the same however some invalid input arguments are included
        """

        #playerTurn.Player1 is 'O'. If you  wish to 'X' then you need to select playerTurn.Player2.
        #Either player can go first regardless of the symbol.
        #Player 1 will always be console and is hardcoded.
        #Format of tuple (player, goFirst, player2Type)
        expectedValues = ((playerTurn.Player1, True, playerType.Random),
                    (playerTurn.Player2, False, playerType.Console),
                    (playerTurn.Player1, False, playerType.Random),
                    (playerTurn.Player2, True, playerType.Console))

        for expected in expectedValues:
            self.assertSequenceEqual(expected, tictactoeFromConsoleBuilder.__fromConsole__())


        assert mockinput.call_count == 18

    def test__factoryCreatePlayer__(self):

        grid = tictactoeGrid()

        actualPlayer = TictactoeGameBuilder.__factoryCreatePlayer__(grid, playerTurn.Player1, playerType.Random)

        self.assertIsInstance(actualPlayer, RandomPlayer)
        self.assertEqual(actualPlayer.board, grid)
        self.assertEqual(actualPlayer.turn, playerTurn.Player1)

        actualPlayer = TictactoeGameBuilder.__factoryCreatePlayer__(grid, playerTurn.Player2, playerType.Console)
        self.assertIsInstance(actualPlayer, ConsolePlayer)
        self.assertEqual(actualPlayer.board, grid)
        self.assertEqual(actualPlayer.turn, playerTurn.Player2)

                                          #Player 1 to be O, go first and play against Random player
    @patch('builtins.input', side_effect=['O', 'Y', '1'
                                         #Player 1 to be X, go second and play against Console player
                                          ,'X', 'N', '2'
                                         #Player 1 to be O, go second and play against Random player
                                          ,'O', 'N', '1'
                                        #Player 1 to be X, go first and play against Console player
                                          ,'X', 'Y', '2'])

    def test_getGameConfig(self, mockinput):
        """
        Method tests the functionality of the getGameConfig method of the tictactoeFromConsoleBuilder
        class against expected values
        """

        expectedValues = ((playerTurn.Player1, True, playerType.Random),
                    (playerTurn.Player2, False, playerType.Console),
                    (playerTurn.Player1, False, playerType.Random),
                    (playerTurn.Player2, True, playerType.Console))

        expectedP2Values = ((RandomPlayer, playerTurn.Player2),
                              (ConsolePlayer, playerTurn.Player1),
                              (RandomPlayer, playerTurn.Player2),
                              (ConsolePlayer, playerTurn.Player1))

        gameBuilder = tictactoeFromConsoleBuilder()

        index = 0

        for expected in expectedValues:
            gameConfig = gameBuilder.getGameConfig()
            self.assertSequenceEqual(expected, gameConfig)

            #(self, player1, p1goFirst, p1Type = playerType.Console, p2Type = playerType.Console)
            p1, p2, grid = gameBuilder.createGame(player1=gameConfig[0], p1goFirst=gameConfig[1],
                                                   #Player1 type will always be console
                                                   p1Type=playerType.Console, p2Type=gameConfig[2])

            #Test values for player 1. We can get values from gameConfig
            self.assertIsInstance(p1, ConsolePlayer)
            self.assertEqual(p1.turn, gameConfig[0])

            #Test Values for player 2.
            expectedP2type, expectedP2Turn = expectedP2Values[index]
            self.assertIsInstance(p2, expectedP2type)
            self.assertEqual(p2.turn, expectedP2Turn)



            #For this to work p1's grid and p2's grid must be the same reference. In otherwords
            #They play with the same grid. As well as equals we can use id() to verify the reference
            #are the same.

            self.assertEqual(p1.board.grid, p2.board.grid)
            self.assertEqual(id(p1.board.grid), id(p2.board.grid))

            #Finally verify who goes first. If its player 1 (user) and they selected O (playerTurn.Player1) then
            #it would be playerTurn.Player1. However if player 1 goes second then player 2 must go first.

            #gameConfig[1] is boolean value indicating if p1 goes first. The turn attribute of the tictactoeGrid class
            #contains the turn of the next player.

            if gameConfig[1]:
                self.assertEqual(grid.turn, expectedValues[index][0])
            else:
                self.assertEqual(grid.turn, playerTurn((expectedValues[index][0].value + 1) % 2))

            index += 1

        assert mockinput.call_count == 12





if __name__ == '__main__':
    unittest.main()

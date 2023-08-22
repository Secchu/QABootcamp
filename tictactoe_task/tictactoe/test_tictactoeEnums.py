"""
Enum classes are any class that inherits from Enum. An Enum class are classes that contain integer variables that
represent different states of an object. This module tests the functionality of the Enum classes used in the
tictactoe console application. Note even though Enum classes are mainly integer values in Python it is possible
to have Enum classes of any types. The tictactoe console application makes use of Enum classes that are ints and
strings.
"""

import unittest
from tictactoeEnums import playerTurn, gameState, gridState, playerSymbol
from tictactoeGrid import tictactoeMove

class testtictactoeEnums(unittest.TestCase):
    def testEnumValues(self):
        """
        This method test the Enum values used in the different Enum classes against expected values.
        """
        self.assertEqual(playerTurn.Player1.value, 0, f"{playerTurn.Player1} enum test FAILED")
        self.assertEqual(playerTurn.Player2.value, 1, f"{playerTurn.Player2} enum test FAILED")
        self.assertEqual(gameState.Player1Win.value, 1, f"{gameState.Player1Win} enum test FAILED")
        self.assertEqual(gameState.Player2Win.value, 2, f"{gameState.Player2Win} enum test FAILED")
        self.assertEqual(gameState.Draw.value, 3, f"{gameState.Draw} enum test FAILED")
        self.assertEqual(gameState.Incomplete.value, 0, f"{gameState.Incomplete} enum test FAILED")

    def testEnumReadOnlyProps(self):
        """
        Some Enum values are getters and are readonly. This method tests that 
        a AttributeError is raised when attempting to assign a value to a readonly
        Enum getter.
        """
        move = tictactoeMove(playerTurn.Player1, 1)
        objAttributes = (("player", move), ("move", move))

        #Test for existence of attribute
        for attribute, obj in objAttributes:
            self.assertTrue(hasattr(obj, attribute))

        #With read only attributes we should get an AttributeError when trying
        #to assign a value to the attribute
        with self.assertRaises(AttributeError):
            move.move = 2

        with self.assertRaises(AttributeError):
            move.player = playerTurn.Player1

    def testPlayerTurnStr(self):
        """
        This method tests the PlayerTurn Enum return expected string when 
        the Enum is converted to a string.
        """
        self.assertEqual(str(playerTurn.Player1),  "Player 1")
        self.assertEqual(str(playerTurn.Player2),  "Player 2")

    def testPlayerSymbolStr(self):
        """
        This method tests the value of the playerSymbol enum values against expected values.
        The symbols should return 'O' or 'X' when converted to string
        """
        self.assertEqual(str(playerSymbol.Player1),  "O")
        self.assertEqual(str(playerSymbol.Player2),  "X")
        self.assertEqual(str(playerSymbol.Unoccupied),  " ")

    def testGameStateStr(self):
        """
        This method tests the expected string values of the gameState
        Enum class when it is converted to string.
        """
        self.assertEqual(str(gameState.Draw), "Draw")
        self.assertEqual(str(gameState.Incomplete), "Incomplete")
        self.assertEqual(str(gameState.Player1Win), "Player 1 Win")
        self.assertEqual(str(gameState.Player2Win), "Player 2 Win")

if __name__ == '__main__':
    unittest.main()
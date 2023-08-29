"""
This module contains the custom defined error classes used in the tictactoe console application.
"""

class gridOccupiedError(Exception):
    def __init__(self, message):
        super().__init__(message)

class gameAlreadyCompletedError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidEndGameState(Exception):
    def __init__(self, message):
        super().__init__(message)
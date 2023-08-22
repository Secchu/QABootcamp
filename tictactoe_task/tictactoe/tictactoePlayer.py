from abc import ABC, abstractmethod
from tictactoeGrid import tictactoeGrid
from tictactoeEnums import playerTurn

class NotMyTurnError(Exception):
    def __init__(self, message):
        super().__init__(message)

class tictactoePlayer(ABC):

    def __init__(self, board, turn=playerTurn.Player1):
        self.board = board
        self.turn = turn

    @abstractmethod
    def getMove(self):
        pass

    def placeMove(self):

        if self.board.turn != self.turn:
            raise NotMyTurnError("Please be patient and wait for your turn before placing your move")

        move = self.getMove()
        self.board.make_move(move)









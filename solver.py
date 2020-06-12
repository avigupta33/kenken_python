from board import Board
from typing import Tuple

class Solver:
    def __init__(self):
        pass

    @staticmethod
    def getFirstBlank(board: Board) -> Tuple[int, int]:
        for i in range(board.size):
            for j in range(board.size):
                if board.getValue(i,j) == 0:
                    return i, j

    def solve(self, board: Board) -> bool:
        unassigned = self.getFirstBlank(board)
        if not unassigned:
            return True
        if board.verify():
            return True
        for num in range(1, board.size + 1):
            if board.isValid(unassigned[0], unassigned[1], num):
                board.setValue(unassigned[0], unassigned[1], num)
                if self.solve(board):
                    return True
                board.setValue(unassigned[0], unassigned[1], 0)

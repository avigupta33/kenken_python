from board import Board
from typing import Tuple

class Solver:
    def __init__(self):
        pass

    def solve(self, board: Board) -> bool:
        pass

class SudokuSolver(Solver):
    def __init__(self):
        pass

    @staticmethod
    def getFirstBlank(board: Board) -> Tuple[int, int]:
        for i in range(board.size):
            for j in range(board.size):
                if board.getValue(i,j) == 0:
                    # print(f"returning {i}, {j}")
                    return i, j

    def solve(self, board: Board) -> bool:
        unassigned = self.getFirstBlank(board)
        if not unassigned:
            # print("finishing here2")
            return True
        if board.verify():
            # print("finishing here")
            return True
        for num in range(1, board.size + 1):
            # print(f"trying {unassigned},  {num}")
            if board.isValid(unassigned[0], unassigned[1], num):
                board.setValue(unassigned[0], unassigned[1], num)
                # print(f"solve setting {unassigned} to {num}")
                if self.solve(board):
                    # print("finishing here3")
                    return True
                board.setValue(unassigned[0], unassigned[1], 0)

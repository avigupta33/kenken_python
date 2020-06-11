from typing import List, Tuple
from square import Square
from board import Board

class Cage:
    def __init__(self, board: Board, operator: str, goal: int, squares: List[Tuple[int,int]]) -> None:
        self.board = board
        self.operator = operator
        self.goal = goal
        self.squares = squares


    def verify(self) -> bool:
        if self.operator = "x":


    def verifyValue(self, value: int) -> bool:
        for row in self.data:
            for val in row:
                if val == value:
                    return False
        return True

    def isInCage(self, row_i: int, col_i: int) -> bool:
        if self.top_left[0]<=row_i<self.top_left[0]+self.cage_size:
            if self.top_left[1]<=col_i<self.top_left[1]+self.cage_size:
                return True
        return False

    def setFromAbsolute(self, row_i: int, col_i: int, val: int) -> None:
        self.data[row_i - self.top_left[0]][col_i - self.top_left[1]] = val


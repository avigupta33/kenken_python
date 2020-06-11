from typing import List, Tuple
from board import Board
from functools import reduce

class Cage:
    def __init__(self, board: Board, operator: str, goal: int, squares: List[Tuple[int,int]]) -> None:
        self.board = board
        self.operator = operator
        self.goal = goal
        self.squares = squares #squares are stored as row_i, col_i

    def getValue(self, coords: Tuple[int, int]) -> int: #coords is row_i, col_i
        return self.board.getValue(coords[0], coords[1])

    def verify(self) -> bool:
        if self.operator == "x":
            product = reduce((lambda x, y: x*y), map(self.getValue, self.squares))
            return product == self.goal





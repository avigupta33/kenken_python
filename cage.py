from typing import List, Tuple
from square import Square
from board import Board

class Cage:
    def __init__(self, board: Board, operator: str, goal: int, squares: List[Tuple[int,int]]) -> None:
        self.board = board
        self.operator = operator
        self.goal = goal
        self.squares = squares

    def getData(self, row_i, c):


    def verify(self) -> bool:
        if self.operator = "x":





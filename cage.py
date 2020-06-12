from typing import List, Tuple
from functools import reduce

class Cage:
    def __init__(self, operator: str, goal: int, squares: List[Tuple[int,int]]) -> None:
        self.operator = operator
        self.goal = goal
        self.squares = squares #squares are stored as row_i, col_i

    def getValue(self, data: List[List[int]], coords: Tuple[int, int]) -> int: #coords is row_i, col_i
        return data[coords[0]][coords[1]]

    def isFull(self, data: List[List[int]]) -> bool:
        for square in self.squares:
            if self.getValue(data, square) == 0:
                return False

        return True

    def isValid(self, data) -> bool:
        if self.isFull(data):
            return self.verify(data)
        return True

    def verify(self, data) -> bool:
        if self.operator == "g":
            if len(self.squares) > 1:
                return False
            else:
                return self.getValue(data, self.squares[0]) == self.goal

        if self.operator == "+":
            return self.sum(data) == self.goal

        if self.operator == "*":
            return self.product(data) == self.goal

        if self.operator == "-":
            if len(self.squares) !=  2:
                return False
            else:
                diff = abs(self.getValue(data, self.squares[0]) - self.getValue(data, self.squares[1]))
                return diff == self.goal

        if self.operator == "/":
            if len(self.squares) != 2:
                return False
            else:
                v0  = self.getValue(data, self.squares[0])
                v1 = self.getValue(data, self.squares[1])
                if v0 == 0 or v1 == 0:
                    return 0
                q = max(v0 / v1, v1/v0)
                return q == self.goal


    def sum(self, data) -> int:
        return reduce((lambda x, y: x + y),
                      [self.getValue(data, s) for s in self.squares])

    def product(self, data) -> int:
        return reduce((lambda x, y: x * y),
                      [self.getValue(data, s) for s in self.squares])

    def display(self) -> None:
        print(f"Cage with op {self.operator} and goal {self.goal} containing {self.squares}")








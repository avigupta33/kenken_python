from typing import List, Tuple
from functools import reduce

class Cage:
    def __init__(self, operator: str, goal: int, squares: List[Tuple[int,int]]) -> None:
        self.operator = operator
        self.goal = goal
        self.squares = squares #squares are stored as row_i, col_i

    def getValue(self, data: List[List[int]], coords: Tuple[int, int]) -> int: #coords is row_i, col_i
        return data[coords[0]][coords[1]]

    def verify(self, data) -> bool:
        if self.operator == "g":
            if len(self.squares) > 1:
                return False
            else:
                return self.getValue(data, self.squares[0]) == self.goal

        if self.operator == "+":
            product = reduce((lambda x, y: x+y), [self.getValue(data, s) for s in self.squares ])
            return product == self.goal

        if self.operator == "*":
            product = reduce((lambda x, y: x*y), [self.getValue(data, s) for s in self.squares ])
            return product == self.goal

        if self.operator == "-":
            if len(self.squares) !=  2:
                return False
            else:
                diff = reduce((lambda x, y: abs(x-y)), [self.getValue(data, s) for s in self.squares ])
                return diff == self.goal

        if self.operator == "/":
            if len(self.squares) != 2:
                return False
            else:
                q1 = reduce((lambda x, y: x/y), [self.getValue(data, s) for s in self.squares ])
                q2 = reduce((lambda x, y: y/x), [self.getValue(data, s) for s in self.squares ])

                return max(q1, q2) == self.goal

    def display(self) -> None:
        print(f"Cage with op {self.operator} and goal {self.goal} containing {self.squares}")








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

    def isValid(self, data, coords):
        if self.isFull(data):
            # print("this case reached")
            return self.verify(data)
        if self.operator == '*':
            if self.goal % self.getValue(data, coords) != 0:
                # print("failing here")
                return False

            if self.product(data) > self.goal:
                # print("failing here2")
                return False

        if self.operator == '+':
            if self.sum(data) > self.goal:
                # print("failing here3")
                return False

        # print(f"cage with op {self.operator} ret True at coords {coords}")
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
                # print("exit 9")
                return False
            else:
                diff = abs(self.getValue(data, self.squares[0]) - self.getValue(data, self.squares[1]))
                # print("Diff: ", diff)
                # print("Goal: ", self.goal)
                # print("Returning", diff == self.goal)
                return diff == self.goal

        if self.operator == "/":
            if len(self.squares) != 2:
                return False
            else:
                q = max(self.getValue(data, self.squares[0]) / self.getValue(data, self.squares[1]),
                        self.getValue(data, self.squares[1]) / self.getValue(data, self.squares[0]))
                # print("Quot.: ", q)
                # print("Goal: ", self.goal)
                # print("Returning", q == self.goal)
                return q == self.goal


    def sum(self, data):
        return reduce((lambda x, y: x + y),
                      [self.getValue(data, s) for s in self.squares])

    def product(self, data):
        return reduce((lambda x, y: x * y),
                      [self.getValue(data, s) for s in self.squares])

    def display(self) -> None:
        print(f"Cage with op {self.operator} and goal {self.goal} containing {self.squares}")








from typing import List
from cage import Cage

class Board:
    def __init__(self, data: List[List[int]], size: int, cages: List[Cage]):
        self.data = data
        self.size = size
        self.cages = cages

    def getValue(self, row_i: int, col_i: int) -> int:
        return self.data[row_i][col_i]

    def setValue(self, row_i: int, col_i: int, value: int) -> None:
        self.data[row_i][col_i] = value


    def isValid(self, row_i: int, col_i: int, value: int) -> bool:
        if row_i < 0 or col_i <0 or row_i >= self.size or col_i >= self.size:
            # print(f"isValid for {value} @ ({row_i}, {col_i}) failed boundary")
            return False

        if value in self.data[row_i]:
            # print(f"isValid for {value} @ ({row_i}, {col_i}) failed row")

            return False

        for i in range(0, self.size):
            if self.data[i][col_i] == value:
                # print(f"isValid for {value} @ ({row_i}, {col_i}) failed col")

                return False

        return True


    def verify(self) -> bool:
        if not self.verifyRows():
            return False
        if not self.verifyCols():
            return False
        if not self.verifyCages():
            return False
        return True

    def verifyRows(self):
        for row in self.data:
            if len(set(row)) != len(row):
                return False
        return True

    def verifyCols(self) -> bool:
        for col_ind in range(self.size):
            col = set()
            for row in self.data:
                if row[col_ind] in col:
                    return False

                else:
                    col.add(row[col_ind])
        return True

    def verifyCages(self) -> bool:
        for cage in self.cages:
            if not cage.verify(self.data):
                return False
        return True

    def display(self) -> None:
        for i in range(0, self.size):
            for j in range(0, self.size):
                print(self.data[i][j], end=" ")
            print()

    def displayCages(self):
        for cage in self.cages:
            cage.display()




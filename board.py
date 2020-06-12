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
        # print(f"SetValue {row_i, col_i} to {value}")
        self.data[row_i][col_i] = value

    def findCage(self, row_i: int, col_i: int)  -> Cage:
        for cage in self.cages:
            if (row_i, col_i) in cage.squares:
                return cage

    def isValid(self, row_i: int, col_i: int, value: int) -> bool:
        if row_i < 0 or col_i <0 or row_i >= self.size or col_i >= self.size:
            # print(f"isValid for {value} @ ({row_i}, {col_i}) failed boundary")
            # print("e 1")
            return False

        if value in self.data[row_i]:
            # print(f"isValid for {value} @ ({row_i}, {col_i}) failed row")
            # print("e 2")
            return False

        for row_i2 in range(0, self.size):
            if self.data[row_i2][col_i] == value:
                # print(f"isValid for {value} @ ({row_i}, {col_i}) failed col")
                # print("e 3")
                return False

        cage = self.findCage(row_i, col_i)
        temp = self.getValue(row_i, col_i)
        ret = True
        # print(f"isValid setting {row_i, col_i} to {value}")
        self.setValue(row_i, col_i, value)
        if not cage.isValid(self.data, (row_i, col_i)):
            ret = False

        self.setValue(row_i, col_i, temp)
        # print(f"isValid2 setting {row_i, col_i} to {temp}")

        return ret


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




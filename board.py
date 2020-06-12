from typing import List, Tuple
from cage import Cage

class Board:
    def __init__(self, data: List[List[int]], size: int, cages: List[Cage]):
        self.data = data
        self.size = size
        self.cages = cages

    def getValue(self, coords: Tuple[int, int]) -> int:
        return self.data[coords[0]][coords[1]]

    def setValue(self, coords: Tuple[int, int], value: int) -> None:
        self.data[coords[0]][coords[1]] = value

    def findCage(self, coords: Tuple[int, int]) -> Cage:
        for cage in self.cages:
            if coords in cage.squares:
                return cage

    def isValid(self, coords: Tuple[int, int], value: int) -> bool:
        row_i, col_i = coords
        if row_i < 0 or col_i <0 or row_i >= self.size or col_i >= self.size:
            return False

        if value in self.data[row_i]:
            return False

        for row_i2 in range(0, self.size):
            if self.data[row_i2][col_i] == value:
                return False

        cage = self.findCage(coords)
        temp = self.getValue(coords)
        ret = True
        self.setValue(coords, value)
        if not cage.isValid(self.data):
            ret = False

        self.setValue(coords, temp)

        return ret

    def verify(self) -> bool:
        if not self.verifyRows():
            return False
        if not self.verifyCols():
            return False
        if not self.verifyCages():
            return False
        return True

    def verifyRows(self) -> bool:
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

    def displayCages(self) -> None:
        for cage in self.cages:
            cage.display()




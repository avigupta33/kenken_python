from typing import List
from cage import Cage

class Board:
    def __init__(self, data: List[List[int]], size: int, cages: List[Cage]):
        self.data = data
        self.size = size
        self.cages = cages

    def getValue(self, row_i: int, col_i: int):
        return self.data[row_i][col_i]

    def verify(self):
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
                print("Failed on rows")
                return False
        return True

    def verifyCols(self):
        for col_ind in range(self.size):
            col = set()
            for row in self.data:
                if row[col_ind] in col:
                    print("Failed on cols")
                    return False

                else:
                    col.add(row[col_ind])
        return True

    def verifyCages(self):
        for cage in self.cages:
            if not cage.verify():
                print("Failed on cage")
                return False
        return True




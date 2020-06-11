from typing import List
from cage import Cage

class Board:
    def __init__(self, data: List[List[int]], size: int):
        self.data = data
        self.size = size
        self.cage_size = int(size**0.5)
        self.cages = self.splitIntoCages()

    def setData(self, row_i: int, col_i: int, value: int) -> None:
        self.data[row_i][col_i] = value
        cage = self.findCage(row_i, col_i)
        cage.setFromAbsolute(row_i, col_i, value)

    def splitIntoCages(self) -> List[List[int]]:
        cages = []
        cage_size = int(self.size**0.5)
        for i in range(0, cage_size):
            for j in range(0, cage_size):
                cage = []
                rows = self.data[i*cage_size:(i+1)*cage_size]
                for row in rows:
                    cage.append(row[j*cage_size:(j+1)*cage_size])
                cages.append(Cage(cage, (i*cage_size,j*cage_size), cage_size))

        return cages

    def findCage(self, row_i: int, col_i: int) -> Cage:
        for cage in self.cages:
            if cage.isInCage(row_i, col_i):
                return cage

        print("Error in findCage")
        return None

    def display(self) -> None:
        for i in range(0, self.size):
            if i % self.cage_size == 0:
                print("-" * 25)
            for j in range(0, self.size):
                if j % self.cage_size == 0:
                    print("|", end=" ")
                print(self.data[i][j], end=" ")

            print("|")
        print("-" * 25)

    def verify(self) -> bool:
        for i in range(self.size):
            row = self.data[i]
            if len(set(row)) != len(row):
                # print(f"Verify failed on row {i}")
                return False

        for col_ind in range(self.size):
            col = []
            for row_ind in range(self.size):
                col.append(self.data[row_ind][col_ind])

            if len(set(col)) != len(col):
                # print(f"Verify failed on col {i}")
                return False

        for i in range(len(self.cages)):
            cage = self.cages[i]
            if not cage.verify():
                # print(f"Verify failed on cage {i} with top left {cage.top_left}")
                return False

        return True

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

        curr_cage = self.findCage(row_i, col_i)

        if not curr_cage.verifyValue(value):
            # print(f"isValid for {value} @ ({row_i}, {col_i}) failed cage")
            return False

        return True







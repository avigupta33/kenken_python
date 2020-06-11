from typing import List

class Board:
    def __init__(self, data: List[List[int]], size: int):
        self.data = data
        self.size = size

    def getValue(self, row_i: int, col_i: int):
        return self.data[row_i][col_i]





from cage import Cage
from board import Board

if __name__ == "__main__":
    data = [[1,2,3],
            [3,1,2],
            [2,3,1]]
    placeholder = Board(data= data, size = 3)
    squares = [(0,0), (1,0), (2,0)]
    cage = Cage(board = placeholder, operator="x", goal = 6, squares=squares)
    print(cage.verify())


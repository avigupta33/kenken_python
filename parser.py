from board import Board
from cage import Cage

class Parser:
    def __init__(self):
        pass

    def parse(self, filename: str) -> Board:
        with open(filename) as fil:
            size_line = fil.readline()
            size_line.strip()
            size = int(size_line)
            cages = []
            line = fil.readline()
            while line:
                row = line.split()
                goal = row[0]
                op = row[1]
                squares = []
                for i in range(2, len(row), 2):
                    squares.append((int(row[i]), int(row[i+1])))

                cages.append(Cage(op, goal, squares))
                line = fil.readline()

            data = [[0 for _ in range(size)] for _ in range(size)]
            board = Board(data, size, cages)

            return board

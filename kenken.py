from solver import Solver
from parser import Parser

if __name__ == "__main__":
    parser = Parser()
    solver = Solver()
    board = parser.parse("puzzles/kenken_test2.txt")
    solver.solve(board)
    board.display()
    print(board.verify())





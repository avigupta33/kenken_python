from cage import Cage
from board import Board
from solver import SudokuSolver
from parser import Parser

if __name__ == "__main__":
    parser = Parser()
    solver = SudokuSolver()
    board = parser.parse("puzzles/kenken_test2.txt")
    solver.solve(board)
    board.display()
    print(board.verify())





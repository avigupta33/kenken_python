from cage import Cage
from board import Board

if __name__ == "__main__":
    data = [[1,2,3],
            [3,1,2],
            [2,3,1]]
    placeholder = Board(data= data, size = 3)

    test_squares = {}
    test_cages = {}

    test_squares["g"] = [(0,1)]
    test_cages["g"] = Cage(board = placeholder, operator="g", goal = 2, squares=test_squares["g"])

    test_squares["+"] = [(0, 0), (1, 1), (2, 2)]
    test_cages["+"] = Cage(board=placeholder, operator="+", goal=3, squares=test_squares["+"])

    test_squares["*"] = [(0,0), (1,0), (2,0)]
    test_cages["*"] = Cage(board = placeholder, operator="*", goal = 6, squares=test_squares["*"])

    test_squares["-"] = [(0, 2), (2, 2)]
    test_cages["-"] = Cage(board=placeholder, operator="-", goal=2, squares=test_squares["-"])

    test_squares["/"] = [(0, 1), (2, 2)]
    test_cages["/"] = Cage(board=placeholder, operator="/", goal=2, squares=test_squares["/"])

    for op in test_cages:
        print(f"For operator {op}, verify is {test_cages[op].verify()}")



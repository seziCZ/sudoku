from src.sudoku import Sudoku
from pprint import pprint

# sample assignment
assignment = [
    [None, 8, 5, None, None, None, None, None, 9],
    [7, None, 4, 5, 8, None, 1, None, None],
    [None, None, None, None, None, None, None, 3, 8],
    [None, 2, 6, 8, 1, None, None, None, 5],
    [8, None, None, None, None, 4, 7, 2, None],
    [None, 7, None, None, None, None, None, 9, 1],
    [None, None, None, 9, None, None, None, None, None],
    [None, None, None, None, 7, None, 9, 1, None],
    [1, 9, None, 6, None, None, None, 5, None],
]

if __name__ == "__main__":
    """
    Script's entry point.
    """
    instance = Sudoku(assignment)
    pprint(instance.solve().grid)

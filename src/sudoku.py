from typing import Set


class Sudoku:
    """
    Minimalist implementation of a backtracking Sudoku solving algorithm
    See https://en.wikipedia.org/wiki/Sudoku_solving_algorithms
    """

    COORDINATES = [(x, y) for y in range(9) for x in range(9)]
    VALUES = set(range(1, 10))

    def __init__(self, grid):
        """
        Constructor.
        :param grid: Representation of the board
        """
        super().__init__()
        self.grid = grid

    def get_row_candidates(self, row: int) -> Set[int]:
        """
        Yields collection of values that are missing in referenced row
        :param row: Index of a row whose missing values are to be found
        :return: Collection of values that are missing in the row
        """
        return self.VALUES.difference(self.grid[row])

    def get_column_candidates(self, column: int) -> Set[int]:
        """
        Yields collection of values that are missing in referenced column
        :param column: Index of a column whose missing values are to be found
        :return: Collection of values that are missing in the column
        """
        actual = [r[column] for r in self.grid]
        return self.VALUES.difference(actual)

    def get_tile_candidates(self, row: int, column: int) -> Set[int]:
        """
        Yields collection of values that are missing in referenced tile
        :param row: Index of a row, associated with a tile whose values are to be found
        :param column: Index of a column.  associated with a tile whose values are to be found
        :return: Collection of values that are missing in the row
        """
        start_row, start_col = int(row / 3) * 3, int(column / 3) * 3
        return self.VALUES.difference({
            self.grid[r][c]
            for r in range(start_row, start_row + 3)
            for c in range(start_col, start_col + 3)
        })

    def get_candidates(self, row: int, column: int) -> Set[int]:
        """
        Yields collection of values that could be associated with provided coordinates.
        :param row: Row coordinate whose allowed values are to be found
        :param column: Row coordinate whose allowed values are to be found
        :return: Collection of values that could be used at given coordinate
        """

        # no candidate if already set
        if self.grid[row][column]:
            return set()

        # yield candidates
        return self.get_row_candidates(row).intersection(
            self.get_column_candidates(column).intersection(
                self.get_tile_candidates(row, column)
            )
        )

    def solve(self) -> 'Sudoku':
        """
        Solves this sudoku, inline.
        :return: Solved sudoku, None if there is no solution
        """

        # identify cell with the least candidates, cease processing if no such cell exists
        blanks = [(row, col) for (row, col) in self.COORDINATES if not self.grid[row][col]]
        weights = [self.get_candidates(row, col) for (row, col) in blanks]
        cells = sorted(zip(blanks, weights), key=lambda entry: len(entry[1]))
        if not cells:
            return self

        # test cell's candidates
        ((row, column), candidates) = cells[0]
        for candidate in candidates:
            self.grid[row][column] = candidate
            if self.solve():
                return self

        # none of the candidates worked, reset
        self.grid[row][column] = None
        return None


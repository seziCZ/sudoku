import unittest

from src.sudoku import Sudoku


class SudokuTest(unittest.TestCase):
    """
    Collection of Sudoku class unit tests.
    """

    ASSIGNMENT = [
        [None, None, 6, None, 2, None, 7, None, 9],
        [4, None, None, 3, None, 7, 8, 5, 6],
        [7, None, None, None, None, 5, None, None, 4],
        [None, None, 2, None, 7, None, None, 8, None],
        [None, 8, None, 2, None, None, 3, 6, None],
        [6, None, 7, 5, None, 8, 9, None, None],
        [None, 1, None, None, None, 3, 5, None, 8],
        [9, None, 5, None, None, None, None, None, None],
        [None, None, 8, 4, 5, 9, None, 7, None]
    ]

    def test_valid(self):
        """
        Smoke test that validates Sudoku class functionality.
        """

        # SETUP
        instance = Sudoku(self.ASSIGNMENT)
        exp_result = [
            [8, 5, 6, 1, 2, 4, 7, 3, 9],
            [4, 2, 1, 3, 9, 7, 8, 5, 6],
            [7, 9, 3, 6, 8, 5, 1, 2, 4],
            [1, 3, 2, 9, 7, 6, 4, 8, 5],
            [5, 8, 9, 2, 4, 1, 3, 6, 7],
            [6, 4, 7, 5, 3, 8, 9, 1, 2],
            [2, 1, 4, 7, 6, 3, 5, 9, 8],
            [9, 7, 5, 8, 1, 2, 6, 4, 3],
            [3, 6, 8, 4, 5, 9, 2, 7, 1]
        ]

        # ACT
        result = instance.solve().grid

        # ASSERT
        self.assertEqual(exp_result, result)


if __name__ == '__main__':
    unittest.main()

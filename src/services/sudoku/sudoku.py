from valid_Numbers import invalid_row_numbers
from valid_Numbers import invalid_column_numbers
from valid_Numbers import invalid_box_numbers
from valid_Numbers import valid_random_number
from difficulties import random_points
import copy

class Sudoku:

    def __init__(self, rows_length: int, columns_length: int):
        self.rows_length = rows_length
        self.columns_length = columns_length
        self.original_matrix = self._matrix_reset()
        self.game_matrix = self._matrix_reset()
        self.generator_time = 0


    def _matrix_reset(self) -> list:
        matrix = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        return matrix


    def _create_game_matrix(self, difficulty):
        self.game_matrix = copy.deepcopy(self.original_matrix)
        random_points(self.game_matrix, difficulty, self.rows_length, self.columns_length)


    def matrix_generator(self) -> bool:
        # This funtion creates a random sudoku matrix at self.original_matrix

        # Every time matrix_generator() executes, reset self.original_matrix
        self.original_matrix = self._matrix_reset()

        for row in range(self.rows_length):
            for column in range(self.columns_length):
                valid_number = valid_random_number(
                    invalid_row_numbers(self.original_matrix, row, self.rows_length),
                    invalid_column_numbers(self.original_matrix, column, self.columns_length),
                    invalid_box_numbers(self.original_matrix, (column, row))
                )
                
                # valid_number == 0 means that there is no valid number at all, so return False
                if valid_number == 0:
                    return False

                self.original_matrix[row][column] = valid_number
        return True


    def matrix_format(self) -> dict:
        # Return Sudoku info as a JSON format 
        out = {
            "generator_time": self.generator_time,
            "rows_length": self.rows_length,
            "columns_length": self.columns_length,
            "original_matrix": self.original_matrix,
            "game_matrix": self.game_matrix,
        }
        return out

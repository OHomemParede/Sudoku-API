from Valid_Numbers import valid_row_numbers
from Valid_Numbers import valid_column_numbers
from Valid_Numbers import valid_box_numbers
from Valid_Numbers import valid_random_number


EXIT_SUCCESS = 0
EXIT_FAILURE = 1

def matrix_generator():
    m = [
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
    for y in range(0, 9):
        for x in range(0, 9):
            number = valid_random_number(
                valid_row_numbers(m, y),
                valid_column_numbers(m, x),
                valid_box_numbers(m, (x, y))
            )
            if number == 0:
                return EXIT_FAILURE, []
            m[y][x] = number
    return EXIT_SUCCESS, m



def matrix_format(m: list):
    out = {}
    c = 1
    for mRow in m:
        out[f'vector{str(c)}'] = mRow[:]
        c+=1
    return out


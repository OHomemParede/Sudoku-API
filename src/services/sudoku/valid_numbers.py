from random import sample


def invalid_row_numbers(matrix: list, row: int, column_length: int) -> list:
    # receives a [matrix] and a reference [row]
    # return a list of invalid numbers in the row.

    invalid_numbers = list()
    for column in range(column_length):
        # matrix[row][column] != 0 means that matrix[row][column] is an invalid
        # number in the row.
        if matrix[row][column]: 
            invalid_numbers.append(matrix[row][column])
    return invalid_numbers



def invalid_column_numbers(matrix: list, column: int, row_length: int) -> list:
    # receives a [matrix] and a reference [column]
    # return a list of invalid numbers in the column.

    invalid_numbers = list()
    for row in range(row_length):
        # matrix[row][column] != 0 means that matrix[row][column] is an invalid
        # number in the column.
        if matrix[row][column]:
            invalid_numbers.append(matrix[row][column])
    return invalid_numbers



def invalid_box_numbers(matrix: list, point: tuple) -> list:
    # receives a [matrix] and a reference [point](column, row)
    # return a list of invalid numbers in box.
    # A box is a 3x3 matrix inside the main sudoku matrix,
    # you can see a better definition at: https://en.wikipedia.org/wiki/Mathematics_of_Sudoku

    invalid_numbers = list()
    column = point[0]
    row = point[1]
    box = {
        0: (0, 1, 2), # 0 <= [column || row] <= 2   
        1: (3, 4, 5), # 3 <= [column || row] <= 5     
        2: (6, 7, 8)  # 6 <= [column || row] <= 8 
    }
    for y in box[ int(row/3) ]:
        for x in box[ int(column/3) ]:
            # matrix[y][x] != 0 means that matrix[y][x]
            # is an invalid number in the box (relative 3x3 matrix).
            if matrix[y][x]:
                invalid_numbers.append(matrix[y][x])
    invalid_numbers =  list(set(invalid_numbers))
    return invalid_numbers



def valid_random_number(*invalid_numbers_rol: tuple) -> int:
    # gets severals invalid numbers.
    # A: return a random number, from 1 to 9, that is not in the row, column or box
    # return 0 if it cant return A

    invalid_numbers = list()
    for numbers in invalid_numbers_rol:
        invalid_numbers.extend(numbers)

    invalid_numbers = set(invalid_numbers)
    valid_numbers_list = list(range(1, 10))


    for number in invalid_numbers:
        valid_numbers_list.remove(number)

    try:
        # if length of valid_numbers_list is zero, raises an erro. 
        return sample(valid_numbers_list, 1)[0]
    except:                                         
        return 0
    

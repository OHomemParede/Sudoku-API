from sudoku import Sudoku
import sys
from time import time


EXIT_SUCCESS = 0
EXIT_FAILURE = 1


rows_length = 9
columns_length = 9


def main(argv):
    if len(argv) != 2:
        print(f"\nSyntax Erro: \n   {argv[0]} [difficulty]\n\n   [difficulty] must be an integer | 0<=[difficulty]<= 81\n")
        return EXIT_FAILURE
    try:
        difficulty = int(argv[1])
        if not 0<=difficulty<=81:
            raise Exception
    except:
        print(f"\nParameter Erro: \n   {argv[0]} [difficulty] \n\n   [difficulty] must be an integer | 0<=[difficulty]<= 81\n")
        return EXIT_FAILURE


    sudoku = Sudoku(rows_length, columns_length)

    # Eventually, it will return a valid set of sudoku numbers
    start_time = time()
    while not sudoku.matrix_generator():
        pass
    sudoku.generator_time = time() - start_time
    
    sudoku._create_game_matrix(difficulty)
    print(sudoku.matrix_format(), end='')

    return EXIT_SUCCESS


if __name__ == '__main__':
    main(sys.argv)

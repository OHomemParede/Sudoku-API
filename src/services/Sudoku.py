from Matrix import matrix_generator
from Matrix import matrix_format
from Difficulties import random_points
import sys

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

def main(argv):
    if len(argv) != 2:
        print(f"\nSyntax Erro: \n   {argv[0]} [valor]\n")
        exit(EXIT_FAILURE)
    try:
        valor = int(argv[1])
        if not 0<=valor<=81:
            raise Exception
    except:
        print(f"\nParameter Erro: \n   {argv[0]} [valor] \n\n   [valor] must be an integer | 0<=[valor]<= 81\n")
        exit(EXIT_FAILURE)

    tag = 1
    while tag:
        tag, m = matrix_generator()
    
    m = random_points(m, valor)
    m = matrix_format(m)
    print(m, end='')
    return EXIT_SUCCESS


if __name__ == '__main__':
    main(sys.argv)

from random import randint

def random_points(matrix: list, difficulty: int, row_length, column_length):
    chosen_points = []
    for k in range(difficulty):
        y = randint(0, row_length-1)
        x = randint(0, column_length-1)
        while [x,y] in chosen_points: 
            y = randint(0, row_length-1)
            x = randint(0, column_length-1)
        chosen_points.append([x,y])
        matrix[y][x] = 0

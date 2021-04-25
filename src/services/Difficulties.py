from random import randint

def random_points(m, n: int):
    chosen_points = []
    for k in range(n):
        y = randint(0, 8)
        x = randint(0, 8)
        while [x,y] in chosen_points: 
            y = randint(0, 8)
            x = randint(0, 8)
        chosen_points.append([x,y])
        m[y][x] = 0
    return m

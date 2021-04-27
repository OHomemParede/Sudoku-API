from random import sample

def valid_row_numbers(m: list, row: int):
    v = list()
    for x in range(9):
        if m[row][x] == 0:
            continue
        v.append(m[row][x])
    return v



def valid_column_numbers(m: list, column: int):
    v = list()
    for y in range(9):
        if m[y][column] == 0:
            continue
        v.append(m[y][column])
    return v



def valid_box_numbers(m: list, ponit: tuple):
    v = list()
    point_x = ponit[0] #column
    point_y = ponit[1] #row
    box = {
        0: (0, 1, 2), # 0<=d<=2     # where [d] is a value of x or a value of y
        1: (3, 4, 5), # 3<=d<=5     # a chave é a divisao inteira de (x ou y) por 3
        2: (6, 7, 8)  # 6<=d<=8 
    }
    for y in box[int(point_y/3)]:
        for x in box[int(point_x/3)]:
            if m[y][x] == 0:
                continue
            v.append(m[y][x])
    return v



def valid_random_number(*arg: list):
    v = list()
    for k in arg:
        v.extend(k)
    v = set(v)
    valid_numbers_list = sample(range(1, 10), 9)
    for a in v:
        valid_numbers_list.remove(a)
    try:
        return sample(valid_numbers_list, 1)[0] # <- returning a random number from valid_numbers_list
    except:                                         
        return 0 # zero means: length of valid_numbers_list is zero, raising an erro.
    
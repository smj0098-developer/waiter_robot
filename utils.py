import math
from hashlib import md5
from CellType import CellType


def create_table(rows, cols, init_value=CellType.EMPTY):
    return [[init_value for _ in range(cols)] for _ in range(rows)]


def print_table(table):
    for row in table:
        print(row)
    # Empty row
    print()


def get_game_table(actual_table_rows, actual_table_cols):

    # we will insert 2-length dividers around the actual map as a boundary-check solution
    rows = actual_table_rows + 4
    cols = actual_table_cols + 4

    # Initialize some variables based on table size
    costs = create_table(rows, cols, -1)
    config = create_table(rows, cols)
    robot_location = (-1, -1)
    butters_count = 0

    divider_character = CellType.BlOCK

    # Insert dividers
    for c in range(cols):
        config[0][c] = divider_character
        config[1][c] = divider_character
        config[rows - 1][c] = divider_character
        config[rows - 2][c] = divider_character
    for r in range(rows):
        config[r][0] = divider_character
        config[r][1] = divider_character
        config[r][cols - 1] = divider_character
        config[r][cols - 2] = divider_character

    for r in range(actual_table_rows):
        row = input().split(' ')
        for c in range(actual_table_cols):
            el = row[c]
            map_r = r + 2
            map_c = c + 2

            if (str.isnumeric(el)):
                costs[map_r][map_c] = int(el)
            elif (el == CellType.BlOCK):
                costs[map_r][map_c] = -1
                config[map_r][map_c] = CellType.BlOCK

            else:
                cost = int(el[0])
                character = el[1]
                costs[map_r][map_c] = cost

                if (character == CellType.ROBOT):
                    robot_location = (map_r, map_c)
                else:
                    if (character == CellType.BUTTER):
                        butters_count += 1
                    config[map_r][map_c] = character

    return costs, config, robot_location, butters_count


def tuple_sum(tuple1, tuple2):
    return tuple([sum(tup) for tup in zip(tuple1, tuple2)])


def get_manhattan_distance(tuple1, tuple2):
    return abs(tuple1[0]-tuple2[0]) + abs(tuple1[1]-tuple2[1])


def hash_iterable(iterable):
    # Can Hash list & tuple
    iterable_str = str(iterable)
    return md5(iterable_str.encode('utf-8')).hexdigest()


def print_algorithm_name(algorithm_name):
    print(f"========= {algorithm_name} =========")

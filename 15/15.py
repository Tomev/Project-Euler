import time


class PositionData:
    positionsData = []
    value = 0

    def __init__(self, pos, val):
        self.positionsData = pos
        self.value = val


positionsData = []
columns_num = 20
rows_num = 20


def list_contains_position_data(position):
    global positionsData

    if len(positionsData) == 0:
        return False

    # print(positionsData)

    for posData in positionsData:
        if position[0] == posData.positionsData[0] and position[1] == posData.positionsData[1]:
            return True

    return False


def get_position_data_from_list(position):
    global positionsData

    for posData in positionsData:
        if position[0] == posData.positionsData[0] and position[1] == posData.positionsData[1]:
            return posData.value

    print("Returning -1")

    return -1


# Extreme programming should be use for better performance
def get_number_of_possible_paths_from_position(position):
    return move_down_if_possible(position[:]) + move_right_if_possible(position[:])


def is_at_end(position):

    global rows_num
    global columns_num

    if position[0] == rows_num or position[1] == columns_num:
        return True
    return False


def move_right_if_possible(position):

    global positionsData

    position[1] += 1

    # print(position)

    if list_contains_position_data(position):

        result = get_position_data_from_list(position)

    else:

        result = 1 if is_at_end(position) else move_down_if_possible(position[:]) + move_right_if_possible(position[:])
        positionsData += [PositionData(position, result)]

    print(position, ", ", result)

    return result


def move_down_if_possible(position):

    global positionsData

    position[0] += 1

    # print(position)

    if list_contains_position_data(position):

        result = get_position_data_from_list(position)

    else:

        result = 1 if is_at_end(position) else move_down_if_possible(position[:]) + move_right_if_possible(position[:])
        positionsData += [PositionData(position, result)]

    print(position, ", ", result)

    return result


start_time = time.time()

print("Counting dynamic...")

my_position = [0, 0]

print(get_number_of_possible_paths_from_position(my_position[:]))

# print(get_number_of_possible_paths(myGrid, 0, 0))

elapsed_time = time.time() - start_time

print("Elapsed time: ", elapsed_time)

# Combinatorial


def factorial(a):

    if a == 0:
        return 1

    result = 1

    for i in range(1, a + 1):
        result *= i

    return result


def binomial_coefficient(a, b):

    result = factorial(a)
    result /= factorial(a-b) * factorial(b)

    return result


start_time = time.time()

print("Counting combinatorial...")

print(binomial_coefficient(rows_num + columns_num, rows_num))

elapsed_time = time.time() - start_time

print("Elapsed time: ", elapsed_time)

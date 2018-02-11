import time


def get_number_of_possible_paths(grid, row, column):
    retval = 0

    if can_go_down(grid, row, column):
        retval += get_number_of_possible_paths(grid, row + 1, column)
    else:
        return 1
    if can_go_right(grid, row, column):
        retval += get_number_of_possible_paths(grid, row, column + 1)
    else:
        return 1

    return retval

    #if can_go_down(grid, row) and can_go_right(grid, column, row):
        #retval = get_number_of_possible_paths(grid, row + 1, column)
        #retval += get_number_of_possible_paths(grid, row, column + 1)
        #return retval

    #else:
        #return 1


def can_go_down(grid, row, column):
    if column > len(grid[0]):
        return False
    if row < len(grid):
        return True

    return False


def can_go_right(grid, row, column):
    if row >= len(grid):
        return False
    if column < len(grid[row]):
        return True

    return False


start_time = time.time()

#myGrid = [[0 for x in range(20)] for y in range(20)]
#myGrid = []

#for x in range(1, 2):

#    myRow = []

#    for y in range(0, x):

#        myRow.append(0)

#    myGrid.append(myRow)

#print(myGrid[19])
#print(myGrid)


myGrid = [[0 for x in range(20)] for y in range(20)]

#print(myGrid)

print("Counting...")

print(get_number_of_possible_paths(myGrid, 0, 0))

elapsed_time = time.time() - start_time

print("Elapsed time: ", elapsed_time)

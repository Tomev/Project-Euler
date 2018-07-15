from math import sqrt
import time

def is_integral(number):
    return number % 1 == 0


def are_integral(numbers):
    for number in numbers:
        if not is_integral(number):
            return False

    return True

# Requires an iterable container with 3 values
# Currently not used
def form_right_angle_triangle(numbers):
    numbers = sorted(numbers)
    if pow(numbers[0], 2) + pow(numbers[1], 2) == pow(numbers[2], 2):
        return True

    return False


def get_potential_solutions(p, solutions):
    for i in range(1, p):
        for j in range(1, p):
            solution = [i, j, sqrt(pow(i, 2) + pow(j, 2))]
            #print(solution)
            if sum(solution) > p:
                break
            if sum(solution) != p:
                continue
            if not are_integral(solution):
                continue
            #print("Adding to solutions")
            solutions.add(tuple(sorted(solution)))



start = time.time()

min_perimeter = 1
max_perimeter = 1001

max_solutions_size = 0
max_solutions_perimeter = 0

solutions_set = set()

for p in range(min_perimeter, max_perimeter):
    solutions_set.clear()

    get_potential_solutions(p, solutions_set)

    #print(p)

    if solutions_set.__len__() > max_solutions_size:
        max_solutions_size = solutions_set.__len__()
        max_solutions_perimeter = p

elapsed_time = time.time() - start

print(max_solutions_size)
print(max_solutions_perimeter)
print('Time: ' + str(elapsed_time))

import time
from methods import get_nth_triangle_number, is_pentagonal, is_hexagonal

start = time.time()

desired_number = 0
current_number = 0
n = 286

while True:
    current_number = get_nth_triangle_number(n)

    if is_hexagonal(current_number) and is_pentagonal(current_number):
        desired_number = current_number
        break

    n += 1

elapsed_time = time.time() - start

print(desired_number)
print('Time: ' + str(elapsed_time))

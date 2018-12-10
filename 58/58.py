from methods import is_prime
from time import time

elapsed_time = time()

current_last = 1

side_len = 1

travel_by = 1

edges_num = 0
prime_edges_num = 0
ratio = 1

while ratio > 0.1:
    side_len += 2
    edges_num += 4
    current_last += 1
    current_last += travel_by
    travel_by += 1

    if is_prime(current_last):
        prime_edges_num += 1

    for i in range(0, 3):
        current_last += travel_by

        if is_prime(current_last):
            prime_edges_num += 1

    travel_by += 1
    ratio = prime_edges_num / edges_num

print(side_len)
elapsed_time = time() - elapsed_time
print('Time: ' + str(elapsed_time))

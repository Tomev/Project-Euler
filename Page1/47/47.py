from methods import get_number_of_factors, has_only_prime_factors
import time

start_time = time.time()

number_of_consecutive_integers = 4
number_of_distinct_prime_factors = 4
current_consecutive_integers = []

i = 2

while len(current_consecutive_integers) < number_of_consecutive_integers:
    if get_number_of_factors(i) == number_of_distinct_prime_factors and has_only_prime_factors(i):
        current_consecutive_integers.append(i)
    else:
        current_consecutive_integers.clear()

    i += 1


elapsed_time = time.time() - start_time

print(current_consecutive_integers)
print('Time: ' + str(elapsed_time))

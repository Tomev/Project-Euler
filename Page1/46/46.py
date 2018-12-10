from methods import is_prime
import time

primes_found = []


def is_sum_of_prime_and_twice_a_square(number):

    if is_prime(number):
        primes_found.append(number)
        return False

    for prime in primes_found:
        power_base = 0
        current_sum = 0

        while current_sum < number:
            power_base += 1
            current_sum = prime + 2 * power_base * power_base

        if current_number == current_sum:
            return True

    return False


start_time = time.time()
desired_number = 0
current_number = 3

while True:
    if is_prime(current_number):
        primes_found.append(current_number)
        current_number += 2
        continue

    if not is_sum_of_prime_and_twice_a_square(current_number):
        break

    current_number += 2

desired_number = current_number

elapsed_time = time.time() - start_time

print(desired_number)
print('Time: ' + str(elapsed_time))

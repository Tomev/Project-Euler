import time
from methods import is_prime, get_permutations

chars_set = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

max_pandigital_prime = 0

while max_pandigital_prime == 0:
    current_permutations = get_permutations(chars_set)
    while len(current_permutations) > 0:
        if is_prime(int(max(current_permutations))):
            max_pandigital_prime = int(max(current_permutations))
            break

        current_permutations.remove(max(current_permutations))
        print(len(current_permutations))
    chars_set.remove(max(chars_set))

print(max_pandigital_prime)






'''
start = time.time()

# Only primes up to 9 digits are interesting.
min_number = 3
max_number = 999999999

max_pandigital_prime = 0

for number in range(max_number, min_number + 1, -2):
    # Iterate from the end. First to find is desired number.
    if is_prime(number) and is_pandigital_from_1_to_n(str(number), len(str(number))):
        max_pandigital_prime = number
        break

elapsed_time = time.time() - start
print(max_pandigital_prime)
print('Time: ' + str(elapsed_time))
'''

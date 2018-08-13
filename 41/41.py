import time
from methods import is_prime, get_permutations


def reduce_set_to_possible_primes(numbers_set):
    number_to_remove = set()
    for number in numbers_set:
        numbers_last_char = number[len(number) - 1]
        if int(numbers_last_char) % 2 == 0 or int(numbers_last_char)  == 5:
            number_to_remove.add(number)
    for number in number_to_remove:
        numbers_set.remove(number)


start = time.time()

chars_set = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

max_pandigital_prime = 0

while max_pandigital_prime == 0:
    current_permutations = get_permutations(chars_set)
    reduce_set_to_possible_primes(current_permutations)
    while len(current_permutations) > 0:
        if is_prime(int(max(current_permutations))):
            max_pandigital_prime = int(max(current_permutations))
            break

        current_permutations.remove(max(current_permutations))
        # print(len(current_permutations))
    chars_set.remove(max(chars_set))

elapsed_time = time.time() - start

print(max_pandigital_prime)
print('Time: ' + str(elapsed_time))

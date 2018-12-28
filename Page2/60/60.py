import sys
sys.path.append('../..')
from methods import get_next_prime, is_prime, get_n_len_distinct_lists
from time import time
from itertools import combinations


def unordered_concatenation_creates_prime(str1, str2):
    return is_prime(int(str1 + str2)) and is_prime(int(str2 + str1))


def create_pairs_of_concatenated_strings(primes):
    for i in range(0, len(primes)):
        for j in range(i + 1, len(primes)):
            if not unordered_concatenation_creates_prime(str(primes[i]), str(primes[j])):
                return False
    return True


elapsed_time = time()

primes = []
current_prime = 2
number_of_objects_in_combination = 5

while current_prime < 700:
    current_prime = get_next_prime(current_prime + 1)
    primes.append(current_prime)

cmb = combinations(primes, number_of_objects_in_combination)

for combination in cmb:
    if create_pairs_of_concatenated_strings(list(combination)):
        print(str(combination) + ": " + str(sum(list(combination))))




#print('Getting combinations')
#combinations = get_n_len_distinct_lists(5, primes)
#print('Got')
'''
print('Looking through combinations')
for combination in combinations:
    if create_pairs_of_concatenated_strings(combination):
        print(combination)
'''

#sum_of_primes = 0

#for prime in solution_primes:
#   sum_of_primes += prime

#print(sum_of_primes)
elapsed_time = time() - elapsed_time
print('Time: ' + str(elapsed_time))

import sys
sys.path.append('../..')
from methods import get_next_prime, is_prime
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


def add_to_dictionary(main_dict, obj_list):
    if len(obj_list) == 0:
        return

    obj_list.sort()
    key = obj_list[0]

    if not key in main_dict:
        main_dict[key] = dict()

    add_to_dictionary(main_dict[key], obj_list[1:])


def get_list_from_key(main_dict, key):

    if len(main_dict[key].keys()) == 0:
        return [[key]]

    lists = []

    for k in main_dict[key].keys():
        for l in get_list_from_key(main_dict[key], k):
            l.append(key)
            lists.append(l)

    return lists


elapsed_time = time()

primes = []
current_prime = 2
number_of_objects_in_combination = 5
solution_primes = []
prime_twos = []
prime_threes = []
prime_fours = []

primes_dict = dict()

while current_prime < 27000:

    current_prime = get_next_prime(current_prime + 1)
    primes.append(current_prime)

    print(current_prime)

    for key in primes_dict:
        l = get_list_from_key(primes_dict, key)
        for primes_list in l:
            primes_list.append(current_prime)
            if create_pairs_of_concatenated_strings(primes_list):
                add_to_dictionary(primes_dict, primes_list)

    for key in primes_dict:
        if len(get_list_from_key(primes_dict, key)[0]) == 5:
            print(get_list_from_key(primes_dict, key))

    add_to_dictionary(primes_dict, [current_prime])


for key in primes_dict:
    if len(get_list_from_key(primes_dict, key)) == 5:
        print(get_list_from_key(primes_dict, key))












'''
print(primes_dict[3].keys())


for key in primes_dict:
    print(get_list_from_key(primes_dict, key))


cmbs = list(set(combinations(primes, 2)))

for combination in cmbs:
    if create_pairs_of_concatenated_strings(list(combination)):
        l = list(combination)
        l.sort()
        prime_twos.append(l)

for primes_two in prime_twos:
    for prime in primes:
        if primes_two.__contains__(prime):
            continue
        primes_two.append(prime)
        if create_pairs_of_concatenated_strings(primes_two):
            prime_threes.append(primes_two[:])
        primes_two.remove(prime)

for primes_three in prime_threes:
    for prime in primes:
        if primes_three.__contains__(prime):
            continue
        primes_three.append(prime)
        if create_pairs_of_concatenated_strings(primes_three):
            primes_three.sort()
            prime_fours.append(primes_three[:])
        primes_three.remove(prime)

#print(set(prime_fours))

cmb = combinations(primes, 4)
cmb = set(cmb)

print(len(list(cmb)))






while len(solution_primes) == 0:

    current_prime = get_next_prime(current_prime + 1)
    primes.append(current_prime)

    if current_prime < 670:
        continue



    for combination in cmbs:
        print(combination)




print(sum(solution_primes))
elapsed_time = time() - elapsed_time
print('Time: ' + str(elapsed_time))
'''

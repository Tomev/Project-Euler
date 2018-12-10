from methods import get_next_prime, is_prime, get_n_len_combinations
import time

replaceable_positions_combinations = []
possible_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
occurred_primes = set()


def find_replaceable_positions_combinations(str_length):
    if str_length < 2:
        return {}

    considered_symbols = []

    for i in range(0, str_length): considered_symbols.append(str(i))

    possible_combinations = []

    for i in range(1, str_length): possible_combinations.append(get_n_len_combinations(i, considered_symbols))

    valid_combinations = []

    for i in range(0, len(possible_combinations)):
        for obj in possible_combinations[i]:
            if len(set(obj)) == (i + 1):
                valid_combinations.append(set(obj))

    return valid_combinations


def get_number_of_prime_family_members(prime):

    max_family_size = 0

    for replaceable_char_set in replaceable_positions_combinations:
        current_family_size = get_prime_family_size_after_replacement(prime, replaceable_char_set)

        if current_family_size > max_family_size:
            max_family_size = current_family_size

    return max_family_size


def get_prime_family_size_after_replacement(prime, replaceable_char_set):
    family = []

    for char in possible_chars:

        family_member = str(prime)

        for replaceable_char_position in replaceable_char_set:
            family_member = family_member[:int(replaceable_char_position)] + char + family_member[int(replaceable_char_position) + 1:]

        if family_member[0] == '0':
            continue

        if is_prime(int(family_member)) and len(str(prime)) == len(family_member):
            family.append(family_member)

    # Ugly check for prime inclusion in family
    if str(prime) in family:
        return len(family)

    return 0


start_time = time.time()

max_family_size_occurred = 0
current_prime_family_size = 0
current_prime = 2

while max_family_size_occurred < 8:

    current_prime = get_next_prime(current_prime + 1)
    replaceable_positions_combinations = find_replaceable_positions_combinations(len(str(current_prime)))

    current_prime_family_size = get_number_of_prime_family_members(current_prime)

    if current_prime_family_size > max_family_size_occurred:
        max_family_size_occurred = current_prime_family_size

elapsed_time = time.time() - start_time

print(current_prime)
print('Time: ' + str(elapsed_time))


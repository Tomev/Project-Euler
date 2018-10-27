from methods import get_next_prime, is_prime, get_n_len_combinations


def find_replaceable_positions_combinations(str_length):
    if str_length < 2: return 0

    considered_symbols = []

    for i in range(0, str_length): considered_symbols.append(str(i))

    possible_combinations = []

    for i in range(1, str_length): possible_combinations.append(get_n_len_combinations(i, considered_symbols))

    valid_combinations = []

    for i in range(0, len(possible_combinations)):
        for object in possible_combinations[i]:
            if(len(set(object)) == i + 1):
                valid_combinations.append(set(object))

    return valid_combinations


def find_combinations_of_other_numbers(combinations_len):

    symbols = []

    for i in range(0, 10):
        symbols.append(str(i))

    possible_combinations = get_n_len_combinations(combinations_len, symbols)

    return possible_combinations


def find_frontally_valid_combinations_of_other_numbers(combinations_len):
    possible_combinations = find_combinations_of_other_numbers(combinations_len)

    valid_combinations = []

    for combination in possible_combinations:
        if not combination[0] == '0':
            valid_combinations.append(combination)

    return valid_combinations


def find_back_valid_combinations_of_other_numbers(combinations_len):
    possible_combinations = find_combinations_of_other_numbers(combinations_len)

    valid_combinations = []

    for combination in possible_combinations:
        if not(int(combination) % 2 == 0 or combination[combinations_len -1] == '5'):
            valid_combinations.append(combination)

    return valid_combinations


def find_both_side_valid_combinations_of_other_numbers(combinations_len):
    possible_combinations = find_back_valid_combinations_of_other_numbers(combinations_len)

    valid_combinations = []

    for combination in possible_combinations:
        if not combination[0] == '0':
            valid_combinations.append(combination)

    return valid_combinations


print(find_both_side_valid_combinations_of_other_numbers(4))

current_prime = get_next_prime(10)
current_prime_len = len(str(current_prime))

while current_prime_len < 3:
    current_prime = get_next_prime(current_prime + 1)

    if len(str(current_prime)) > current_prime_len:
        current_prime_len = len(str(current_prime))
        find_replaceable_positions_combinations(current_prime_len)

print(find_replaceable_positions_combinations(len(str(current_prime))))

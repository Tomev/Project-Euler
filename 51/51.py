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


current_prime = get_next_prime(10)
current_prime_len = len(str(current_prime))

while current_prime_len < 7:
    current_prime = get_next_prime(current_prime + 1)

    if len(str(current_prime)) > current_prime_len:
        current_prime_len = len(str(current_prime))
        find_replaceable_positions_combinations(current_prime_len)

print(find_replaceable_positions_combinations(len(str(current_prime))))

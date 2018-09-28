from math import sqrt


# A lot of ifs, so that it potentially works faster
def is_pandigital_from_1_to_n(string, n):
    if len(string) != n:
        return False
    else:
        chars_in_string = set()

        for char in string:
            chars_in_string.add(char)

        if len(chars_in_string) != n:
            return False

        if '0' in chars_in_string:
            return False

        for number in range(1, n + 1):
            if str(number) in chars_in_string:
                continue
            else:
                return False

    return True


def is_prime(num):
    if num == 1:
        return False
    for denominator in range(2, int(sqrt(num)) + 1):
        if num % denominator == 0:
            return False
    return True


def are_primes(numbers):
    for num in numbers:
        if not (is_prime(num)):
            return False
    return True

def get_next_prime(num):
    if num % 2 == 0:
        num += 1

    while not is_prime(num):
        num += 2

    return num


def is_palindrome(string):
    i = 0
    while len(string) - 1 - i > i:
        if string[len(string) - i - 1] != string[i]:
            return False
        i += 1
    return True


def get_permutations(chars_set):
    if len(chars_set) < 2:
        return chars_set

    # Create list of chars so that there's iterable collection
    chars_list = list(chars_set)
    sets_permutations = set()

    for index in range(0, len(chars_list)):
        currently_removed_char = chars_list[0]
        chars_list = chars_list[1:]

        for permutation in list(get_permutations(set(chars_list))):
            sets_permutations.add(str(currently_removed_char) + str(permutation))

        chars_list.append(currently_removed_char)

    return sets_permutations


def get_nth_triangle_number(n):
    return n * (n + 1) / 2


def get_nth_pentagonal_number(n):
    return n * (3 * n - 1) / 2


def get_nth_hexagonal_number(n):
    return n * (2 * n - 1)


def is_triangle(number):
    n = 1
    current_triangle_number = 0
    while current_triangle_number < number:
        current_triangle_number = get_nth_triangle_number(n)
        n += 1
    if current_triangle_number == number:
        return True
    return False


def is_pentagonal(number):
    n = 1
    current_pentagonal_number = 0
    while current_pentagonal_number < number:
        current_pentagonal_number = get_nth_pentagonal_number(n)
        n += 1
    if current_pentagonal_number == number:
        return True
    return False


def is_hexagonal(number):
    n = 1
    current_hexagonal_number = 0
    while current_hexagonal_number < number:
        current_hexagonal_number = get_nth_hexagonal_number(n)
        n += 1
    if current_hexagonal_number == number:
        return True
    return False


def has_only_prime_factors(number):

    if number <= 1:
        return False

    i = 2

    while number != 1:
        if number % i == 0:
            if not is_prime(i):
                return False
            else:
                number = number / i
                i = 2
        else:
            i += 1

    return True


def get_number_of_factors(number):
    factors = set()
    i = 2

    while number > 1:
        if number % i == 0:
            factors.add(i)
            number = number / i
            i = 2
        else:
            i += 1

    return len(factors)


def get_equal_length_combinations(some_string):
    if len(some_string) < 2:
        return some_string

    # Create list of chars so that there's iterable collection
    chars_list = []

    for char in some_string:
        chars_list.append(char)

    sets_permutations = set()

    for index in range(0, len(chars_list)):
        currently_removed_char = chars_list[0]
        chars_list = chars_list[1:]

        for permutation in list(get_equal_length_combinations((chars_list))):
            sets_permutations.add(str(currently_removed_char) + str(permutation))

        chars_list.append(currently_removed_char)

    return sets_permutations


def are_permutations(numbers):

    numbers_chars = []
    last_number_index = -1

    for number in numbers:
        numbers_chars.append([])
        last_number_index += 1
        for a_char in str(number):
            numbers_chars[last_number_index].append(a_char)

    for number_chars in numbers_chars:
        for char in numbers_chars[0]:
            if not number_chars.count(char) == numbers_chars[0].count(char):
                return False

    return True





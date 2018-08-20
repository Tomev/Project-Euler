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


def get_nth_pentagonal_number(n):
    return n * (3 * n - 1) / 2


def is_pentagonal(number):
    n = 1
    current_pentagonal_number = 0
    while current_pentagonal_number < number:
        current_pentagonal_number = get_nth_pentagonal_number(n)
        n += 1
    if current_pentagonal_number == number:
        return True
    return False




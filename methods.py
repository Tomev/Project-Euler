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

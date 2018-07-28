from math import sqrt


def is_prime(num):
    if num <= 1:
        return False
    for denominator in range(2, int(sqrt(num)) + 1):
        if num % denominator == 0:
            return False
    return True


def is_circular_prime(num):
    num_permutations = get_rotations(str(num))

    for permutation in num_permutations:
        if not is_prime(int(permutation)):
            return False
    return True


def get_rotations(string):
    rotations = set()

    offset = 1
    rotation = ''

    while rotation != string:

        rotation = ''

        for i in range(len(string)):
            rotation = rotation + string[(i + offset) % len(string)]

        rotations.add(rotation)
        offset = offset + 1

    return rotations


circular_primes = []
top_limit = 1000000
bottom_limit = 1

for number in range(bottom_limit, top_limit):
    if is_circular_prime(number):
        circular_primes.append(number)

print(circular_primes)
print(len(circular_primes))

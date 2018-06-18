import math


def is_prime(num):
    if num <= 1:
        return False
    for denominator in range(2, int(math.sqrt(num)) + 1):
        if num % denominator == 0:
            return False
    return True


def is_circular_prime(num):
    num_permutations = get_rotations(str(num))

    for permutation in num_permutations:
        if not is_prime(int(permutation)):
            return False
    return True


''' By mistake I made permutations check, not rotation check. I left permutations generator for future use. '''


def get_permutations(string):
    permutations = set()

    permutations.add(string[0])
    string = string.replace(string[0], '', 1)

    while len(string) != 0:
        permutations = get_permutations_of_words_and_letter(permutations, string[0])
        string = string.replace(string[0], '', 1)

    return permutations


def get_permutations_of_words_and_letter(words, letter):
    permutations = set()

    for word in words:
        permutations.update(get_permutations_of_word_and_letter(word, letter))

    return permutations


def get_permutations_of_word_and_letter(word, letter):
    permutations = set()

    for i in range(0, len(word)):

        permutation = str('')

        for j in range(0, len(word)):
            if j == i:
                permutation = permutation + letter
            permutation = permutation + word[j]

        permutations.add(permutation)

    permutations.add(word + letter)

    return permutations


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

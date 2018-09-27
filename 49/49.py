from methods import is_prime, get_next_prime


def are_permutations(numbers):

    numbers_chars = []
    last_number_index = -1

    for number in numbers:
        numbers_chars.append([])
        last_number_index += 1
        for char in str(number):
            numbers_chars[last_number_index].append(char)

    for number_chars in numbers_chars:
        for char in numbers_chars[0]:
            if not number_chars.count(char) == numbers_chars[0].count(char):
                return False


    return True



# Get 4 digit primes
current_prime = get_next_prime(1000)
primes = []

while len(str(current_prime)) < 5:
    primes.append(current_prime)
    current_prime = get_next_prime(current_prime + 1)


for i in range(0, len(primes)):
    for j in range(i + 1, len(primes)):

        primes_diff = int(primes[j]) - int(primes[i])
        third_term = int(primes[j]) + primes_diff

        prime_triplets = []
        prime_triplets.append(int(primes[i]))
        prime_triplets.append(int(primes[j]))
        prime_triplets.append(third_term)

        triplet_satisfies_conditions = True
        triplet_satisfies_conditions = triplet_satisfies_conditions and is_prime(third_term)
        triplet_satisfies_conditions = triplet_satisfies_conditions and are_permutations(prime_triplets)

        if triplet_satisfies_conditions:
            print(prime_triplets)



'''
j = 0

for prime in primes:
    prime_combinations = list(get_equal_length_combinations(str(prime)))

    for i in range(len(prime_combinations) - 1, 0, -1):

        int_combination = int(prime_combinations[i][0])

        if int_combination == 0:
            prime_combinations.pop(i)
        elif not is_prime(int_combination):
            prime_combinations.pop(i)

    if len(prime_combinations) > 2:
        print("%i. %s" % (j, prime_combinations))
        j += 1
'''

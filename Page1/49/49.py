from methods import is_prime, get_next_prime, are_permutations

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

        prime_triplets = [int(primes[i]), int(primes[j]), third_term]

        triplet_satisfies_conditions = True
        triplet_satisfies_conditions = triplet_satisfies_conditions and is_prime(third_term)
        triplet_satisfies_conditions = triplet_satisfies_conditions and are_permutations(prime_triplets)
        triplet_satisfies_conditions = triplet_satisfies_conditions and third_term < 10000

        if triplet_satisfies_conditions:
            print(prime_triplets)


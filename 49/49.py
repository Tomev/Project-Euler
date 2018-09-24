from methods import is_prime, get_next_prime, get_equal_length_combinations

# Get 4 digit primes
current_prime = get_next_prime(1000)
primes = []

while len(str(current_prime)) < 5:
    primes.append(current_prime)
    current_prime = get_next_prime(current_prime + 1)


for prime in primes:
    prime_combinations = get_equal_length_combinations(str(prime))

    for combination in prime_combinations:
        if not len(str(int(combination))) == len(str(prime)):
            prime_combinations.remove(combination)
        if not is_prime(int(combination)):
            prime_combinations.remove(combination)

        print(prime_combinations)



# for prime in primes:


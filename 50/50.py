from methods import get_next_prime, is_prime


# Get all primes below 1 000 000
primes_below_limit = [2]
new_prime = get_next_prime(0)
limit = 1000000

while new_prime < limit:
    primes_below_limit.append(new_prime)
    new_prime = get_next_prime(new_prime + 1)

# Find configuration with longest sum
max_prime_sum = 0
current_prime_sum = 0
summed_primes = []
max_summed_primes_len = 0

for i in range(0, len(primes_below_limit)):

    current_prime_sum = primes_below_limit[i]
    summed_primes = [i]

    for j in range(i + 1, len(primes_below_limit)):
        current_prime_sum += primes_below_limit[j]
        summed_primes.append(i)

        if current_prime_sum > limit:
            break

        if is_prime(current_prime_sum) and max_summed_primes_len < len(summed_primes):
            max_prime_sum = current_prime_sum
            max_summed_primes_len = len(summed_primes)


print(max_prime_sum)
print(max_summed_primes_len)

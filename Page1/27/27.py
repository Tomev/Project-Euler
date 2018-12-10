import math


prime_number_list = []


def is_on_primes_list(num):
    return prime_number_list.__contains__(num)


def is_prime(num):
    if num < 0:
        return False
    if num == 1:
        return False
    for denominator in range(2, int(math.sqrt(num)) + 1):
        if num % denominator == 0:
            return False
    return True


def get_prime_chain_length(a, b):
    i = -1
    while True:
        i += 1
        considered_number = i*i + a*i + b
        if is_on_primes_list(considered_number):
            continue
        elif is_prime(considered_number):
            prime_number_list.append(considered_number)
            continue
        else:
            return i


max_a = 1000
max_b = 1001
longest_chain_a = -max_a
longest_chain_b = -max_b
longest_chain_length = -1


for a in range(-max_a + 1, max_a):
    for b in range(-max_b +1, max_b):
        current_chain_length = get_prime_chain_length(a, b)

        if current_chain_length > longest_chain_length:
            longest_chain_a = a
            longest_chain_b = b
            longest_chain_length = current_chain_length
            print('a = ', a, ', b = ', b)

print('a = ', longest_chain_a)
print('b = ', longest_chain_b)
print('a * b = ', longest_chain_a * longest_chain_b)




import math


def is_prime(num):
    if num == 1:
        return False
    for denominator in range(2, int(math.sqrt(num)) + 1):
        if num % denominator == 0:
            return False
    return True


def is_truncatable_prime(num):
    if not is_prime(num):
        return False
    return is_right_truncatable_prime(num) and is_left_truncatable_prime(num)


def is_right_truncatable_prime(num):
    reduced_num = str(num)
    while len(reduced_num) != 1:
        reduced_num = reduced_num[1:]
        if not is_prime(int(reduced_num)):
            return False
    return True


def is_left_truncatable_prime(num):
    reduced_num = str(num)
    while len(reduced_num) != 1:
        reduced_num = reduced_num[:-1]
        if not is_prime(int(reduced_num)):
            return False
    return True


search_min = 10
search_max = 1000000
truncatable_primes = []

for number in range(search_min, search_max):
    if is_truncatable_prime(number):
        truncatable_primes.append(number)

print(len(truncatable_primes))
print(truncatable_primes)
print(sum(truncatable_primes))

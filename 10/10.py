import math


def is_prime(num):
    if num == 1:
        return False
    for denominator in range(2, int(math.sqrt(num)) + 1):
        if num % denominator == 0:
            return False
    return True

print(sum(i for i in range(3, 2000001, 2) if is_prime(i)) + 2)

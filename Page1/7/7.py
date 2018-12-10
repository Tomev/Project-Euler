import math


def is_prime(num):
    if num == 1:
        return False
    for denominator in range(2, int(math.sqrt(num)) + 1):
        if num % denominator == 0:
            return False
    return True


count = 0
number = 1

while count != 10001:
    number += 1
    if is_prime(number):
        count += 1

print(number)

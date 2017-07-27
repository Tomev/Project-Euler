import math


def is_prime(num):
    if num == 1:
        return False
    for denominator in range(2, int(math.sqrt(num))):
        if num % denominator == 0:
            return False
    return True

number = 600851475143

for i in range(1, int(math.sqrt(number))):
    if is_prime(i) and number % i == 0:
        x = i

print(x)

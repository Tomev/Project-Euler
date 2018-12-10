import math


def count_proper_divisors_sum(number):

    divisors_sum = 0

    for divisor in range(1, math.ceil(number / 2) + 1):
        if number % divisor == 0:
            divisors_sum += divisor

    return divisors_sum


def is_in_amicable_pair(number):

    divisors_sum = count_proper_divisors_sum(number)

    if divisors_sum == number:
        return False

    if count_proper_divisors_sum(divisors_sum) == number:
        return True

    return False


def sum_set_values(numbers_set):

    numbers_sum = 0

    for element in numbers_set:
        numbers_sum += element

    return numbers_sum


amicable_numbers = set()

for i in range(1, 10000):
    if is_in_amicable_pair(i):
        amicable_numbers.add(i)

print(sum_set_values(amicable_numbers))

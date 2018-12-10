import math


def is_sum_of_nth_powers_of_its_characters(num, n):
    powers_sum = 0
    for i in range(0, len(str(num))):
        powers_sum += math.floor(math.pow(int(str(num)[i]), n))
    return powers_sum == num


numbers_sum = 0
power = 5

for number in range(2, math.floor(math.pow(9, power) * 6)):
    if is_sum_of_nth_powers_of_its_characters(number, power):
        numbers_sum += number
        print(numbers_sum)

print(numbers_sum)

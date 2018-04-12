import math

def is_abundant_number(number):
    proper_divisors = find_proper_divisors(number)

    divisors_sum = sum(proper_divisors)

    return divisors_sum > number


def find_proper_divisors(number):
    proper_divisors = []

    for div in range(1, math.floor(number/2) +1):
        if number % div == 0:
            proper_divisors.append(div)

    return proper_divisors


def is_double_abundant_sum(number, abudantNums):

    for i in range(0, abudantNums.__len__()):
        for j  in range(0, abudantNums.__len__()):
            abundant_sum = abudantNums[i] + abudantNums[j]
            if abundant_sum > number:
                break
            if abundant_sum == number:
                return True
    return False


abundant_numbers = []

last_non_double_abundant_sum_number = 28123
all_numbers_considered_sum = 0

print("Finding abundant numbers...")

for i in range(1, last_non_double_abundant_sum_number + 1):
    if is_abundant_number(i):
        abundant_numbers.append(i)
    all_numbers_considered_sum += i

print("Finding sums of two abundant numbers in considered range...")

sums_of_two_abundant_numbers = {24}

for i in range(0, len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        current_abundant_number_sum = abundant_numbers[i] + abundant_numbers[j]
        if current_abundant_number_sum <= last_non_double_abundant_sum_number:
            sums_of_two_abundant_numbers.add(current_abundant_number_sum)

print(all_numbers_considered_sum - sum(sums_of_two_abundant_numbers))

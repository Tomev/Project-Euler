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


abundantNumbers = []

last_non_double_abundant_sum_number = 28123

for i in range(1, last_non_double_abundant_sum_number + 1):
    if is_abundant_number(i):
        abundantNumbers.append(i)

print(abundantNumbers)

sum_of_non_double_abundant_sum_numbers = 0

for i in range(1, last_non_double_abundant_sum_number + 1):
    print(i)
    if not is_double_abundant_sum(i, abundantNumbers):
        sum_of_non_double_abundant_sum_numbers += i

print(sum_of_non_double_abundant_sum_numbers)

def factorial(number):
    fct = 1
    for i in range(2, number + 1):
        fct = fct * i

    return fct


def get_upper_bound():
    upper_bound = 1
    sum_of_9_factorials = factorial(9)

    while upper_bound <= sum_of_9_factorials:
        upper_bound = upper_bound * 10
        sum_of_9_factorials = sum_of_9_factorials + factorial(9)

    return upper_bound


desired_sum = 0

for num in range(3, get_upper_bound() + 1):
    sum_of_digits_factorials = 0

    for digit in str(num):
        sum_of_digits_factorials = sum_of_digits_factorials + factorial(int(digit))

    if num == sum_of_digits_factorials:
        desired_sum = desired_sum + num

print(desired_sum)

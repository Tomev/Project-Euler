import math


def count_number_of_divisors(number):

    divisors_num = 0
    div = 1

    while div <= int(math.sqrt(number)):
        if number % div == 0:
            if div == math.sqrt(number):
                divisors_num += 1
            else:
                divisors_num += 2
        div += 1

    return divisors_num


triangle_number = 1
i = 2

while True:
    div_num = count_number_of_divisors(triangle_number)
    if div_num > 500:
        break
    triangle_number += i
    i += 1

print(triangle_number)

def is_divisible_by_numbers_from_2_to_20(number):
    for divisor in range(2,20):
        if number % divisor != 0:
            return False
    return True

x = 20

while True:
    if is_divisible_by_numbers_from_2_to_20(x):
        break
    x += 20

print(x)
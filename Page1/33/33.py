def is_curious_fraction(numerator, denominator):

    if numerator >= denominator:
        return False

    common_number = get_common_number(numerator, denominator)

    if common_number == "-1":
        return False

    num1 = int(str(numerator).replace(common_number, "", 1))
    num2 = int(str(denominator).replace(common_number, "", 1))

    original_fraction = numerator / denominator
    new_fraction = num1/num2

    if original_fraction == new_fraction:
        return True

    return False


def get_common_number(number1, number2):
    num1 = str(number1)
    num2 = str(number2)

    for num in num1:
        if num2.__contains__(num):
            return num

    return "-1"


min_numerator = 10
max_numerator = 100
min_denominator = 10
max_denominator = 100

curious_fractions = []

# Find curious fractions
for num in range(min_numerator, max_numerator):

    if num % 10 == 0:
        continue

    for denom in range(min_denominator, max_denominator):

        if denom % 10 == 0:
            continue

        if is_curious_fraction(num, denom):
            curious_fractions += [[num, denom]]

# Prepare them in their lowest common terms
for fraction in curious_fractions:
    common_num = get_common_number(fraction[0], fraction[1])
    fraction[0] = int(str(fraction[0]).replace(common_num, "", 1))
    fraction[1] = int(str(fraction[1]).replace(common_num, "", 1))

    i = 2
    while i <= fraction[0]:
        if fraction[0] % i == 0 and fraction[1] % i == 0:
            fraction[0] = int(fraction[0] / i)
            fraction[1] = int(fraction[1] / i)
            i = 1
        i += 1

# Get their product
curious_fractions_product = [1, 1]

for fraction in curious_fractions:
    curious_fractions_product[0] *= fraction[0]
    curious_fractions_product[1] *= fraction[1]

# Simplify their product (as it's necessary for the exercise
i = 2
while i <= curious_fractions_product[0]:
    if curious_fractions_product[0] % i == 0 and curious_fractions_product[1] % i == 0:
        curious_fractions_product[0] = int(curious_fractions_product[0] / i)
        curious_fractions_product[1] = int(curious_fractions_product[1] / i)
        i = 1
    i += 1

print(curious_fractions_product)

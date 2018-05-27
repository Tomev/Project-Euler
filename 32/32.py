def is_pandigital_from_1_to_9(string):
    if len(string) != 9:
        return False
    else:
        chars_in_string = set()

        for char in string:
            chars_in_string.add(char)

        if '0' in chars_in_string:
            return False

        if len(chars_in_string) == 9:
            return True

    return False


distinctive_products = set()

for multiplicand in range(2, 1000000):

    if '0' in str(multiplicand):
        continue

    if len(str(multiplicand)) != len(set(str(multiplicand))):
        continue

    print(multiplicand)

    for multiplier in range(2, 1000000):

        product = multiplicand * multiplier
        string_to_check = str(product) + str(multiplier) + str(multiplicand)

        if len(string_to_check) > 9:
            break

        if is_pandigital_from_1_to_9(string_to_check):
            distinctive_products.add(product)

products_sum = 0

for product in distinctive_products:
    products_sum += product

print(products_sum)

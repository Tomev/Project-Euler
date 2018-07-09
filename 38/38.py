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


search_min = 1
search_max = 10000
largest_number = 0


for number in range(search_min, search_max):
    # There has to be a concatenation
    prod_concatenation = str(number) + str(number * 2)

    multiplier = 3

    while len(prod_concatenation) < 9:
        prod_concatenation = prod_concatenation + str(number * multiplier)
        multiplier = multiplier + 1

    if is_pandigital_from_1_to_9(prod_concatenation):
        if int(prod_concatenation) > largest_number:
            largest_number = int(prod_concatenation)

print(largest_number)

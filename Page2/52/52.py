import time
import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)


def highest_multiplication_has_more_characters(number, multiplications):
    highest_multiplication = max(multiplications) * number

    if len(str(highest_multiplication)) > len(str(number)):
        return True

    return False


def has_same_characters_as_its_multiplications(number, multiplications):

    for multiplication in multiplications:

        if not compare(str(number), str(number * multiplication)):
            return False

    return True



start_time = time.time()

multiplication_coefficients = [6, 5, 4, 3, 2]

current_number = 1


while True:

    if has_same_characters_as_its_multiplications(current_number, multiplication_coefficients):
        break

    current_number += 1

    if highest_multiplication_has_more_characters(current_number, multiplication_coefficients):
        current_number = pow(10, len(str(current_number)))



elapsed_time = time.time() - start_time

print(current_number)
print('Time: ' + str(elapsed_time))

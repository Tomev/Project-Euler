import time
from methods import get_permutations


def satisfies_all_conditions(number):
    if not satisfies_first_condition(number) or \
       not satisfies_second_condition(number) or \
       not satisfies_third_condition(number) or \
       not satisfies_forth_condition(number) or \
       not satisfies_fifth_condition(number) or \
       not satisfies_sixth_condition(number) or \
       not satisfies_seventh_condition(number):
        return False
    return True


# d_2d_3d_4 % 2 == 0
def satisfies_first_condition(number):
    return int(str(number)[3]) % 2 == 0


# d_3d_4d_5 % 3 == 0
def satisfies_second_condition(number):
    number_string = str(number)
    return (int(number_string[2]) + int(number_string[3]) + int(number_string[4])) % 3 == 0


# d_4d_5d_6 % 5 == 0
def satisfies_third_condition(number):
    return int(str(number)[5]) % 5 == 0


# d_5d_6d_7 % 7 == 0
def satisfies_forth_condition(number):
    number_string = str(number)
    return int(number_string[4] + number_string[5] + number_string[6]) % 7 == 0


# d_6d_7d_8 % 11 == 0
def satisfies_fifth_condition(number):
    number_string = str(number)
    return int(number_string[5] + number_string[6] + number_string[7]) % 11 == 0


# d_7d_8d_9 % 13 == 0
def satisfies_sixth_condition(number):
    number_string = str(number)
    return int(number_string[6] + number_string[7] + number_string[8]) % 13 == 0


# d_8d_9d_10 % 17 == 0
def satisfies_seventh_condition(number):
    number_string = str(number)
    if len(number_string) < 10:
        print(number)
    return int(number_string[7] + number_string[8] + number_string[9]) % 17 == 0


start = time.time()

interesting_numbers_sum = 0

chars_set = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])

for permutation in get_permutations(chars_set):
    if str(permutation)[0] == '0':
        continue
    if satisfies_all_conditions(int(permutation)):
        interesting_numbers_sum = interesting_numbers_sum + int(permutation)

elapsed_time = time.time() - start

print(interesting_numbers_sum)
print('Time: ' + str(elapsed_time))


from fractions import Fraction
from time import time

global_denominators = []


def get_n_level_denominator(n):

    global global_denominators
    result = Fraction()

    if len(global_denominators) >= n:
        return global_denominators[n - 1]

    if n == 1:
        result = Fraction(2)
    else:
        result = Fraction(2) + Fraction(1,get_n_level_denominator(n-1))

    global_denominators.append(result)
    return result


number_of_fractions_with_longer_numerator = 0

elapsed_time = time()


for i in range(1, 1000 + 1):
    f = Fraction(1) + Fraction(1, get_n_level_denominator(i))
    if len(str(f.denominator)) < len(str(f.numerator)):
        number_of_fractions_with_longer_numerator += 1

print(number_of_fractions_with_longer_numerator)
elapsed_time = time() - elapsed_time
print('Time: ' + str(elapsed_time))

from methods import is_palindrome
from time import time

def is_lychrel_number(number):
    # Note that this check is valid for number < 10000

    for i in range(1, 50):
        number += int(str(number)[::-1])
        if is_palindrome(str(number)):
            return False

    return True

max_num = 10000
elapsed_time = time()
lychrel_nums_count = 0

for num in range(1, max_num + 1):
    if is_lychrel_number(num):
        lychrel_nums_count += 1


elapsed_time = time() - elapsed_time
print(f'#Lychrel numbers under 10000: {lychrel_nums_count}.')
print('Time: ' + str(elapsed_time))

import time
from methods import get_nth_pentagonal_number, is_pentagonal

start = time.time()

pentagonal_numbers = []
n = 1
desired_pair_found = False
desired_number = 0

while not desired_pair_found:
    new_pentagonal_number = get_nth_pentagonal_number(n)
    n += 1
    for previous_pentagonal_number in pentagonal_numbers:
        pentagonals_sum = previous_pentagonal_number + new_pentagonal_number
        pentagonals_difference = abs(previous_pentagonal_number - new_pentagonal_number)
        if pentagonal_numbers.__contains__(pentagonals_difference) and is_pentagonal(pentagonals_sum):
            desired_pair_found = True
            desired_number = pentagonals_difference
            break
    pentagonal_numbers.append(new_pentagonal_number)


elapsed_time = time.time() - start

print(desired_number)
print('Time: ' + str(elapsed_time))

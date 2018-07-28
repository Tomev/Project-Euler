import time

start = time.time()

concatenated_string = ''

positions_to_find = [1, 10, 100, 1000, 10000, 100000, 1000000]
digits_on_desired_positions = []
list_offset = -1

next_number = 1

while len(concatenated_string) < max(positions_to_find):
    concatenated_string = concatenated_string + str(next_number)
    next_number = next_number + 1

for position in positions_to_find:
    digits_on_desired_positions.append(concatenated_string[position + list_offset])

multiplication = 1

for digit in digits_on_desired_positions:
    multiplication = multiplication * int(digit)

elapsed_time = time.time() - start

print(multiplication)
print('Time: ' + str(elapsed_time))

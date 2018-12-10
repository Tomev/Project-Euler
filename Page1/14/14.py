def get_collatz_sequence_length(number):
    if number == 1:
        return 1
    if number % 2 == 0:
        return 1 + get_collatz_sequence_length(number / 2)
    else:
        return 1 + get_collatz_sequence_length(3* number + 1)


longest_length = 0
longest_length_number = 0

for i in range(1, 1000000):

    length_of_i = get_collatz_sequence_length(i)

    if length_of_i > longest_length:
        longest_length = length_of_i
        longest_length_number = i

print(longest_length_number)

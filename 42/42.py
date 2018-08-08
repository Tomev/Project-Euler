import time


CHAR_OFFSET = 64
TRIANGLE_NUMBERS = set([1])


def is_triangle_word(word):
    word_value = count_word_value(word)

    if max(TRIANGLE_NUMBERS) < word_value:
        n = 1
        while max(TRIANGLE_NUMBERS) <= word_value:
            TRIANGLE_NUMBERS.add(int(0.5 * n * (n + 1)))
            n += 1

    return TRIANGLE_NUMBERS.__contains__(word_value)


def count_word_value(word):
    word_value = 0
    for letter in word:
        word_value += ord(letter) - CHAR_OFFSET

    return word_value


start = time.time()

# Get words from file
file_name = 'problem.txt'
num_lines = sum(1 for line in open(file_name, "r"))
file = open(file_name, "r")
words = file.readline().replace("\"", '').split(',')

# Count number of triangle words
triangle_words_number = 0

for w in words:
    triangle_words_number += 1 if is_triangle_word(w) else 0

elapsed_time = time.time() - start

print(triangle_words_number)
print('Time: ' + str(elapsed_time))

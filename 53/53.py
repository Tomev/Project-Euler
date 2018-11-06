from methods import factorial
import time


def countCombinatoricSelection(string_len, chars_num):
    c = factorial(chars_num)
    c = c / factorial(string_len)
    c = c / factorial(chars_num - string_len)
    return c


start_time = time.time()
greater_than_million_count = 0
start_chars_num = 1
end_chars_num = 100

for n in range(start_chars_num, end_chars_num + 1):
    for r in range(1, n + 1):
        if countCombinatoricSelection(r, n) > 1000000:
            greater_than_million_count += 1

print(greater_than_million_count)
elapsed_time = time.time() - start_time
print('Time: ' + str(elapsed_time))

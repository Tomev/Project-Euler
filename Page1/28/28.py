highest_last_element = 1
result = highest_last_element

for size in range(3, 1002, 2):
    print(size)
    result += 4 * highest_last_element + 10 * (size - 1)
    highest_last_element = highest_last_element + 4 * (size - 1)

print(result)

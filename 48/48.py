numbers_sum = 0

for i in range(1, 1000 + 1):
    numbers_sum += pow(i, i);

print(str(numbers_sum)[len(str(numbers_sum))-10:])

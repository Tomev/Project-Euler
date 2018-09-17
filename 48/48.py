sum = 0

for i in range(1, 1000 + 1):
    sum += pow(i, i);

print(str(sum)[len(str(sum))-10:])

i = 1
j = 0
fib = []

while i < 4000000:
    fib.append(i)
    i, j = j+i, i

print(sum(i for i in fib if i % 2 == 0))

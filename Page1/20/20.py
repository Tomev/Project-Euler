factorial = 1
digitsSum = 0

for i in range(1, 100):
    factorial *= i

while factorial:
    digitsSum += factorial % 10
    factorial //= 10

print(digitsSum)

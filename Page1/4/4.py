def is_palindrome(string):
    i = 0
    while len(string) - 1 - i > i:
        if string[len(string)- i - 1] != string[i]:
            return False
        i += 1
    return True


x = 0

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if is_palindrome(str(i*j)):
            if i * j > x:
                x = i * j

print(x)

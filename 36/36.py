def is_palindrome(string):
    i = 0
    while len(string) - 1 - i > i:
        if string[len(string) - i - 1] != string[i]:
            return False
        i += 1
    return True


limit = 1000000
double_base_palindromes_sum = 0

for number in range(1, limit):
    if is_palindrome(str(number)) and is_palindrome(str(bin(number)).replace('0b', '')):
        double_base_palindromes_sum = double_base_palindromes_sum + number

print(double_base_palindromes_sum)





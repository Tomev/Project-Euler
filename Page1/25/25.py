def find_nth_fibonacci_number(n):
    if n < 2:
        return 1

    fib_last = 1
    fib_current = 1

    for i in range(3, n+1):
        temp = fib_current
        fib_current += fib_last
        fib_last = temp

    return fib_current


def find_index_of_fibonacci_number_with_given_length(length):

    if length == 1:
        return 1

    i = 2
    fib_last = 1
    fib_current = 1

    while len(str(fib_current)) != length:
        i += 1
        temp = fib_current
        fib_current += fib_last
        fib_last = temp

    return i


print(find_index_of_fibonacci_number_with_given_length(1000))

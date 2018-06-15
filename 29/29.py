def get_function_value(a, b):
    result = 1
    for i in range(0, b):
        result *= a
    return result


MIN_A = 2
MAX_A = 100
MIN_B = 2
MAX_B = 100

values_set = set()

for a in range(MIN_A, MAX_A + 1):
    print(a)
    for b in range(MIN_B, MAX_B + 1):
        values_set.add(get_function_value(a,b))

print(len(values_set))

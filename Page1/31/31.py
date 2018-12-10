available_coins = [200, 100, 50, 20, 10, 5, 2, 1]
target = 200
start_coins = 0
possible_combinations = 0


def get_possible_combinations_with_coins_from_n(n, start):
    global available_coins
    global possible_combinations
    global target

    if n == len(available_coins) - 1:
        possible_combinations += 1
        return

    i = 0
    while start < target:
        start += available_coins[n] * i
        if start > target:
            return
        if start == target:
            possible_combinations += 1
            return
        i = 1
        get_possible_combinations_with_coins_from_n(n + 1, start)


get_possible_combinations_with_coins_from_n(0, start_coins)
print(possible_combinations)




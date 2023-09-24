__author__ = "Tomasz Rybotycki"

import sympy as sp
from itertools import combinations


def is_valid_set(s):
    combs = combinations(s, 2)

    for comb in combs:
        if not sp.isprime(int(str(comb[0]) + str(comb[1]))) or not sp.isprime(int(str(comb[1]) + str(comb[0]))):
            return comb

    # Trick to print the results I need fast.
    if len(s) == 5:
        print(s)
        print(sum(s))

    return True


def brute_force():
    primes = sp.sieve.primerange(3, 1000)
    combs = combinations(primes, 5)

    for comb in combs:
        if is_valid_set(comb):
            print(comb)
            print(sum(comb))
            break


def expected():
    # Nothing found.
    primes = sp.sieve.primerange(3, 100000000)

    minimal_4 = (3, 7, 109, 673)

    sets = []

    for prime in primes:
        if prime not in minimal_4:
            sets.append(minimal_4 + (prime,))

    for set in sets:
        if is_valid_set(set):
            print(set)
            print(sum(set))
            break


def get_valid_combinations(primes, n, comb=()):

    if len(comb) == n:
        return [comb]

    combs = []

    for p in primes:

        if len(comb) == 0:
            combs.extend(get_valid_combinations(primes, n, (p,)))
            continue

        if p <= comb[-1]:
            continue

        if is_valid_set(comb + (p,)) == True:
            combs.extend(get_valid_combinations(primes, n, comb + (p,)))

    return combs


def smart():
    primes = list(sp.sieve.primerange(3, 10000))
    primes.pop(1)  # Pop 5

    combs = get_valid_combinations(primes, 5)

    print(combs)


def main():
    # brute_force()
    # expected()  # Nothing found.
    smart()


if __name__ == "__main__":
    main()
    print("Done!")

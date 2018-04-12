def find_all_permutations(symbols):

    permutations = []

    for symbol in symbols:
        reduced_symbols = symbols[:]
        reduced_symbols.remove(symbol)
        sub_permutations = find_all_permutations(reduced_symbols)

        if len(sub_permutations) == 0:
            permutations.append(symbol)
        else:
            for permutation in sub_permutations:
                permutations.append(symbol + permutation)

    return permutations


characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

characters_permutations = find_all_permutations(characters)

characters_permutations.sort()

# -1 is offset, as the list elements starts from 0
print(characters_permutations[1000000 - 1])


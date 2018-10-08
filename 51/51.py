from methods import get_next_prime, is_prime, get_replecable_positions_combinations_from_length

replacable_positions_combinations = []

# Can not replace a part of the number if there is no number, thus on index 0 ...
replacable_positions_combinations.append([])
# Can not replace a part of the number if a number has only one character, thus on index 1...
replacable_positions_combinations.append([])

current_prime = get_next_prime(1)

while(True):
    if(len(str(current_prime)) == len(replacable_positions_combinations)):
        replacable_positions_combinations  = get_replecable_positions_combinations_from_length(len(str(current_prime)))



print(replacable_positions_combinations)

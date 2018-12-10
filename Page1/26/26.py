from decimal import getcontext, Decimal
getcontext().prec = 5000 # High precision is essential here


def get_numbers_decimal_part(number):
    return str(number).split("0.")[1]


def find_recurring_cycle(decimal_part):
    recurring_cycle = ""
    potential_recurring_cycle = ""

    while len(decimal_part) > 0:
        potential_recurring_cycle = decimal_part[0]

        if is_recurring_cycle(potential_recurring_cycle, decimal_part):
            if len(potential_recurring_cycle) > len(recurring_cycle):
                recurring_cycle = potential_recurring_cycle

        for j in range(1, len(decimal_part) - 1):
            potential_recurring_cycle += decimal_part[j]

            if is_recurring_cycle(potential_recurring_cycle, decimal_part):
                # Check if potential recurring cycle is superposition of current recurring cycles
                if recurring_cycle == "":
                    recurring_cycle = potential_recurring_cycle
                if is_recurring_cycle(recurring_cycle, potential_recurring_cycle):
                    break
                else:
                    if len(potential_recurring_cycle) > len(recurring_cycle):
                        recurring_cycle = potential_recurring_cycle

        decimal_part = decimal_part.split(decimal_part[0])[1]

    return recurring_cycle


def is_recurring_cycle(potential_cycle, decimal_part):
    decimal_part_separated_by_potential_cycle = decimal_part.split(potential_cycle)

    if len(decimal_part_separated_by_potential_cycle) < 3:
        return False

    for index in range(0, len(decimal_part_separated_by_potential_cycle) - 1):
        if decimal_part_separated_by_potential_cycle[index] != '':
            return False

    if potential_cycle.find(decimal_part_separated_by_potential_cycle[len(decimal_part_separated_by_potential_cycle) - 1]) == -1:
        return False

    return True


limit = 1001
number_with_longest_recurring_cycle_in_decimal_fraction_part = 0
longest_recurring_cycle_size = 0

for i in range(2, limit):
    current_recurring_cycle = find_recurring_cycle(get_numbers_decimal_part(Decimal(1)/Decimal(i)))
    print(i, ". ", current_recurring_cycle)

    if len(current_recurring_cycle) > longest_recurring_cycle_size:
        longest_recurring_cycle_size = len(current_recurring_cycle)
        number_with_longest_recurring_cycle_in_decimal_fraction_part = i

print("d = ", number_with_longest_recurring_cycle_in_decimal_fraction_part)

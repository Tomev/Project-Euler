# Instead of letters I could very well use their count when returning. That'd be a lot faster, yet less clean.

import math


def get_written_number(number):
    if number < 10:
        return get_written_single_digit_number(number)
    if number < 20:
        return get_written_teen_number(number)
    if number < 100:
        return get_written_double_number(number)
    if number < 1000:
        return get_written_triple_number(number)
    return "one thousand"


def get_written_single_digit_number(number):
    return {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        0: "zero"
    }.get(number, "Not recognized number")


def get_written_teen_number(number):
    return {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }.get(number, "Not recognized number")


def get_written_double_number(number):
    result = ""

    result += get_written_tens_number(math.floor(number / 10))

    if number % 10 > 0:
        result += "-" + get_written_single_digit_number(number % 10)

    return result


def get_written_tens_number(number):
    return{
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }.get(number, "Not recognized tens number")


def get_written_triple_number(number):
    result = ""

    hundreds_number = math.floor(number / 100)
    result += get_written_single_digit_number(hundreds_number) + " hundred"

    if number % 100 > 0:
        result += " and " + get_written_number(number % 100)

    return result


def remove_hyphens(string):
    return string.replace("-", "")


def remove_spaces(string):
    return string.replace(" ", "")


loopStart = 1
loopEnd = 1000
lettersSum = 0

for num in range(loopStart, loopEnd + 1):
    lettersSum += remove_hyphens(remove_spaces(get_written_number(num))).__len__()

print(lettersSum)

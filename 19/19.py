def is_leap_year(year):

    if year % 100 == 0:
        if year % 400 == 0:
            return True
        return False

    return year % 4 == 0


def get_days_num_form_month_number(month, year):

    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28

    if month == 9 or month == 4 or month == 11 or month == 6:
        return 30

    return 31


i_year = 1900
day = 1

# Prepare for year
for i_month in range(1, 12 + 1):
    day = (day + get_days_num_form_month_number(i_month, i_year)) % 7;

sundayStarts = 0

for i_year in range(1901, 2000 + 1):
    for i_month in range(1, 12 + 1):
        if day == 0:
            sundayStarts += 1

        day = (day + get_days_num_form_month_number(i_month, i_year)) % 7;

print(sundayStarts)

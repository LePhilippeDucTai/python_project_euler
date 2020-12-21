def is_leap_year(n):
    return (n % 4 == 0) and ((n % 100 != 0) or (n % 400 == 0))


# Strategy :
# To get : list of all the tuples of
# (year, month, #of the day (from 0 to 6))
# (1901, 1, 2) for example

import itertools as it
import functools as ft


def counting_sundays():
    days_months = lambda year: {
        0: 31,  # January
        1: 28 + is_leap_year(year),  # February
        2: 31,  # March
        3: 30,  # April
        4: 31,  # May
        5: 30,  # June
        6: 31,  # July
        7: 31,  # August
        8: 30,  # September
        9: 31,
        10: 30,
        11: 31,
    }
    # days = it.count()
    tuples_ymd = lambda y1, y2: [
        (year, month + 1, day)
        for year in range(y1, y2)
        for month in range(12)
        for day in range(1, days_months(year)[month] + 1)
    ]
    tuples_ymd_1900 = tuples_ymd(1900, 1901)
    tuples_ymd_1901_2000 = tuples_ymd(1901, 2001)
    all_days_shift = lambda shift, calendar: [
        ((i + shift) % 7, *tup) for i, tup in enumerate(calendar)
    ]
    year_1900 = all_days_shift(0, tuples_ymd_1900)
    shift = year_1900[-1][0] + 1
    years_1901_2000 = all_days_shift(shift, tuples_ymd_1901_2000)
    all_first_of_month = list(
        filter(
            lambda tup: tup[0] == 6, (filter(lambda tup: tup[3] == 1, years_1901_2000))
        )
    )
    print(all_first_of_month)
    print(len(all_first_of_month))


counting_sundays()

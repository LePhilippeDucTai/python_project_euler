import functools as ft


def prod(li):
    return ft.reduce(lambda x, y: x * y, li)


def largest_n_adjacent_digits(num, n):
    s = str(num)
    p = len(s)
    li = [prod(map(lambda y: int(y), s[i : i + n])) for i in range(p - n)]
    return max(li)

import numpy


def sum_squares(n):
    return n * (n + 1) * (2 * n + 1) / 6


def sum_ints(n):
    return n * (n + 1) / 2


def ssq_diff(n):
    return sum_ints(n) ** 2 - sum_squares(n)

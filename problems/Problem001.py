def sum_of_ints(n):
    return n * (n + 1) / 2


def sum_mult_3_5(n):
    return 3 * sum_of_ints(n // 3) + 5 * sum_of_ints(n // 5) - 15 * sum_of_ints(n // 15)


print(sum_mult_3_5(999))

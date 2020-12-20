import functools as ft

from utils import timing

# Collatz sequence generator
def collatz_seq(starting_num):
    divide_by_2 = lambda n: n // 2
    triple_plus_one = lambda n: 3 * n + 1
    collatz = starting_num
    while collatz > 1:
        yield collatz
        collatz = divide_by_2(collatz) if collatz % 2 == 0 else triple_plus_one(collatz)
    yield 1

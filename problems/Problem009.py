import functools as ft
import itertools as it
from utils import timing
import multiprocessing as mp


class ParallelMap:
    def __init__(self):
        self.pool = mp.Pool(4)

    def map(self, f, iter):
        return self.pool.imap_unordered(f, iter, chunksize=100)


def prod(li):
    return ft.reduce(lambda x, y: x * y, li)


def isPythagorean(tup: tuple):
    a, b, c = sorted(tup)
    return a ** 2 + b ** 2 == c ** 2


@timing.time_it
def isPythogorean_condition(cond):
    integers = it.combinations(range(1, 1000), r=3)
    return next(
        prod(triplet)
        for triplet in integers
        if isPythagorean(triplet) and cond(triplet)
    )


print(isPythogorean_condition(lambda triplet: sum(triplet) == 1000))

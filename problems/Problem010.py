from sympy import sieve
import numpy as np
import math
import functools as ft
from utils import timing


@timing.time_it()
def primes_list(n):
    n_to_check = range(2, int(math.sqrt(n)) + 1)
    init_all_numbers = set(range(2, n))
    erastostene = lambda acc, x: acc.difference(range(x * x, n, x))
    return list(ft.reduce(erastostene, n_to_check, init_all_numbers))


def sum_of_primes_list_lt(n):
    return sum(primes_list(n))

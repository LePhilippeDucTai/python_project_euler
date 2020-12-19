import multiprocessing as mp
import functools as ft


def f(x):
    return x * x


def somme(acc, x):
    return acc + x


def mp_ssq(n):
    p = mp.Pool(4)
    x = p.imap_unordered(f, range(n), chunksize=10)
    y = ft.reduce(somme, x)
    return y


def ssq(n):
    x = map(f, range(n))
    y = ft.reduce(somme, x)
    return y

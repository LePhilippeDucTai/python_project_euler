import itertools as it


def fibo_gen(less_than):
    a, b = 1, 2
    yield a
    yield b
    while b <= less_than:
        a, b = b, a + b
        yield b


def even_fib_numbers(n):
    return sum(x for x in fibo_gen(n) if x % 2 == 0)

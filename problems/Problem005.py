import itertools as it
from utils.timing import time_it


@time_it()
def smallest_divisible(a, b):
    N = range(b, a, -1)
    return next(x for x in it.count(start=1) if all(x % i == 0 for i in N))


if __name__ == "__main__":
    print(smallest_divisible(1, 10))

import math
import functools as ft


def primes_list(n):
    n_to_check = range(2, int(math.sqrt(n)) + 1)
    init_all_numbers = set(range(2, n))
    erastostene = lambda acc, x: acc.difference(range(x * x, n, x))
    return list(ft.reduce(erastostene, n_to_check, init_all_numbers))


def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n + 1)]

    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is
        # a prime
        if prime[p] == True:

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return [i for i, b in enumerate(prime) if b == True and i > 1]


def prime_factors(n):
    primes = primes_list(int(math.sqrt(n)))
    return list(x for x in primes if n % x == 0)


def largest_prime_factor(n):
    primes = reversed(primes_list(int(math.sqrt(n))))
    return next(x for x in primes if n % x == 0)


if __name__ == "__main__":
    n = 600851475143
    x = largest_prime_factor(n)
    print(x)

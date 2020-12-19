import itertools as it


def palindromic_number(n):
    s = str(n)
    return s == s[::-1]


def largest_palindrome(k):
    N = range(10 ** k - 1, 10 ** (k - 1), -1)
    return sorted(
        [
            x * y
            for x, y in it.combinations_with_replacement(N, 2)
            if palindromic_number(x * y)
        ]
    )[-1]


if __name__ == "__main__":
    print(largest_palindrome(3))

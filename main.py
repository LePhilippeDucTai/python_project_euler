from problems import Problem014

if __name__ == "__main__":
    collatz_length = lambda number: len(list(x for x in Problem014.collatz_seq(number)))
    print(list(x for x in Problem014.collatz_seq(13)))
    longest_collatz = [(n, collatz_length(n)) for n in range(20)]
    res = sorted(longest_collatz, key=lambda x: x[1])
    print(res[-1])

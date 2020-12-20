from problems import Problem014
import itertools as it


def test_problem014():
    assert [x for x in Problem014.collatz_seq(13)] == [
        13,
        40,
        20,
        10,
        5,
        16,
        8,
        4,
        2,
        1,
    ]

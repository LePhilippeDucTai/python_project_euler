from problems import Problem015
import pytest


@pytest.mark.parametrize("input, expected", [(2, 6), (20, 137846528820)])
def test_problem015(input, expected):
    assert Problem015.number_of_paths(input) == expected

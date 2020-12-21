from problems import Problem009
import pytest


@pytest.mark.parametrize("input, expected", [((3, 4, 5), True), ((5, 6, 7), False)])
def test_problem009(input, expected):
    assert Problem009.isPythagorean(input) == expected

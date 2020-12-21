import pytest
from problems import Problem019


@pytest.mark.parametrize(
    "year, expected",
    [
        (2024, True),
        (2020, True),
        (2023, False),
        (2028, True),
        (2032, True),
        (1999, False),
        (1900, False),
        (1700, False),
        (1881, False),
        (2000, True)
    ],
)
def test_problem019(year, expected):
    assert Problem019.is_leap_year(year) == expected

from problems import Problem003


def test_prime_factors():
    assert set(Problem003.prime_factors(13195)) == set({5, 7, 13, 29})

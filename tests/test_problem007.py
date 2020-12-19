from problems import Problem007


def test_problem007():
    assert Problem007.last_n_prime(6) == 13
    assert Problem007.last_n_prime(10001) == 104743


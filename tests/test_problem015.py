from problems import Problem015


def test_problem015():
    assert Problem015.number_of_paths(2) == 6
    assert Problem015.number_of_paths(20) == 137846528820

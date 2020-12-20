from problems import Problem009


def test_problem009():
    assert Problem009.isPythagorean((3, 4, 5)) == True
    assert Problem009.isPythagorean((5, 6, 7)) == False

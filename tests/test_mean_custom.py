from sp211_21967646_98.mean_custom import mean_custom

def test_mean_custom_basic():
    assert mean_custom([1, 2, 3, 4, 5]) == 3

def test_mean_custom_floats():
    assert mean_custom([1.5, 2.5, 3.5]) == 2.5

def test_mean_custom_negative():
    assert mean_custom([-1, -2, -3]) == -2
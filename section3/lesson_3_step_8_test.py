def f(x):
    return abs(x)

def test_linear_1():
    assert f(1) == 1, "expected 1"

def test_linear_2():
    assert f(2) == 2, "expected 2"

def test_linear_3():
    assert f(3) == 3, "expected 3"

def test_linear_4():
    assert f(-1) == -1, "expected -1"

def test_linear_5():
    assert f(-2) == -2, "expected -2"
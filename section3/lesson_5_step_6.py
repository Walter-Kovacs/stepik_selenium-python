#pytest -v lesson_5_step_6.py
import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True

@pytest.mark.xfail
def test_not_succeed():
    assert False

@pytest.mark.skip
def test_skipped():
    assert False

@pytest.mark.abc
def test_abc1():
    assert True

@pytest.mark.abc
def test_abc2():
    assert True

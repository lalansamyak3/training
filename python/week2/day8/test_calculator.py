import python.week2.day8.calculator as calculator
import pytest
from python.week2.day8.calculator import add, divide, is_even


def test_add():
    assert calculator.add(2, 3) == 5


def test_divide():
    assert calculator.divide(10, 2) == 5
    try:
        calculator.divide(10, 0)
        assert False, "Expected ValueError"
    except ValueError:
        pass


@pytest.mark.parametrize("a,b,expected", [(2, 3, 5), (10, 2, 12)])
def test_add_parametrized(a, b, expected):
    assert calculator.add(a, b) == expected


from python.week2.day8.calculator import is_even


def test_even_number():
    assert is_even(4) is True


def test_odd_number():
    assert is_even(7) is False


def test_zero_is_even():
    assert is_even(0) is True


def test_negative_even():
    assert is_even(-2) is True


def test_negative_odd():
    assert is_even(-3) is False

from hypothesis import given
import hypothesis.strategies as some
from main import add


@given(some.integers(), some.integers())
def test_add_random_integer(x, y):
    result = add(x, y)
    assert result == x + y


@given(some.integers(min_value=5, max_value=10), some.integers(min_value=5, max_value=10))
def test_add_10_20(x, y):
    result = add(x, y)
    assert result >= 10
    assert result <= 20

import pytest
from pytest import approx
from mystatistics import average

@pytest.mark.parametrize("ns, expected", [
    ([0.1, 0.1, 0.1], 0.1)
])
def test_average(ns, expected):
    assert average(ns) == approx(expected, abs = 0.01), f"{ns} equals the expected value of {expected}."

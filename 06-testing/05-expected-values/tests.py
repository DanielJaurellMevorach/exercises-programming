import pytest


@pytest.mark.parametrize("list", [
    [digit for digit in range(1000)]
])
def test_split_in_two(list):
    assert list


pytest.mark.parametrize("left, right", [])
def test_merge_sorted(left, right):
    pass
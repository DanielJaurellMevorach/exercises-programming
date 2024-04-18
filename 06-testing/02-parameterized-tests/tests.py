import pytest
from parentheses import matching_parentheses

# Passing tests
@pytest.mark.parametrize('string', [
    '',
    '()',
    '(())',
    '()()()',
    '(())()',
])
def test_matching_parentheses(string):
    assert matching_parentheses(string), f"{string} has matching parantheses."

# Failing tests
@pytest.mark.parametrize('string', [
    '(',
    ')',
    ')(',
    '(()))(()',
])
def test_uneven_parentheses(string):
    assert not matching_parentheses(string), f"{string} has uneven parantheses."

import pytest
import inspect
from assignment import is_palindrome, is_strictly_ascending

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

# Test cases for is_palindrome
@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 3, 2, 1], True),
    ([1, 2, 3, 4, 5], False),
    ([7, 8, 8, 7], True),
    ([1, 1, 1, 1], True),
    ([], True)
])
def test1(lst, expected):
    assert is_palindrome(lst) == expected
    assert check_contains_loop(is_palindrome)

# Test cases for is_strictly_ascending
@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 3, 4, 5], True),
    ([-5, 10, 99, 123456] , True),
    ([1, 1, 2, 3, 4], False),
    ([4, 5, 6, 7, 3, 7, 9] , False),
    ([2, 3, 3, 4, 5]  , False),
    ([10], True)
])
def test2(lst, expected):
    assert is_strictly_ascending(lst) == expected
    assert check_contains_loop(is_strictly_ascending)

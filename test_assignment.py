import pytest
import inspect
from assignment import cube_elements, remove_duplicates, reverse_list

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3], [1, 8, 27]),
    ([0, 1, 2], [0, 1, 8]),
    ([2, 3, 4], [8, 27, 64]),
    ([-1, -2, -3], [-1, -8, -27]),
    ([2], [8])
])
def test1(numbers, expected):
    assert cube_elements(numbers) == expected
    assert check_contains_loop(cube_elements)

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 2, 3, 4, 4], [1, 2, 3, 4]),
    ([5, 5, 5, 5], [5]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2, 2, 3, 1, 4], [1, 2, 3, 4]),
    ([0, 0, 0], [0])
])
def test2(numbers, expected):
    assert remove_duplicates(numbers) == expected
    assert check_contains_loop(remove_duplicates)

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3], [3, 2, 1]),
    ([4, 5, 6, 7], [7, 6, 5, 4]),
    ([1], [1]),
    ([], []),
    ([10, 20, 30], [30, 20, 10])
])
def test3(numbers, expected):
    assert reverse_list(numbers) == expected
    assert check_contains_loop(reverse_list)


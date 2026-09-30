import pytest
from return_prime_numbers import my_numbers

def test_if_return_contains_list():
    result = my_numbers()
    assert isinstance(result, list)
    assert len(result) > 0


def test_if_return_contains_prime_numbers():
    result = my_numbers()
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert result == expected


def test_if_return_contains_large_list_of_prime_numbers():
    result = my_numbers()
    assert len(result) == 25
import pytest
from return_sum_list import my_numbers

def test_check_if_is_int():
    with pytest.raises(TypeError):
        my_numbers("This is not a list")
    
    with pytest.raises(TypeError):
        my_numbers([])

    with pytest.raises(TypeError):
        my_numbers(None)

    with pytest.raises(TypeError):
        my_numbers({"key":"value"})


def test_if_int_is_zero():
    assert my_numbers(0) == 0


def test_negative_numbers():
    with pytest.raises(TypeError):
        my_numbers(-5)


import pytest
from test_bubble_sort_ import bubble_sort

def test_small_list():

    small_input = [12, 4, 7, 1]
    bubble_sort(small_input)

    assert len(small_input) == 4
    assert sorted(small_input) == small_input


def test_large_list():
    large_input = list(range(101, 0, -1))
    bubble_sort(large_input)
    
    assert large_input == sorted(large_input)
    assert len(large_input) == 101


def test_empty_list():
    empty_input = []
    bubble_sort(empty_input)
    assert len(empty_input) == 0


def test_error_if_notlis():

    with pytest.raises(TypeError):
        bubble_sort("This ain't list")

    with pytest.raises(TypeError):
        bubble_sort(12345)

    with pytest.raises(TypeError):
        bubble_sort(None)

    with pytest.raises(TypeError):
        bubble_sort({"key": "value"})

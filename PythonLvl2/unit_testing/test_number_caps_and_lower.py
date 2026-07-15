import pytest
from number_caps_lower import lower_upper

def test_to_check_if_parameters_are_strings():
    with pytest.raises(TypeError):
        lower_upper(1, 2, 3)
    with pytest.raises(TypeError):
        lower_upper("Hello", 2, "World")
    with pytest.raises(TypeError):
        lower_upper("Hello", "World", None)


def test_to_check_if_parameters_are_not_zero():
    with pytest.raises(TypeError):
        lower_upper(0)


def test_negative_numbers_in_result():
    with pytest.raises(TypeError):
        lower_upper(-1)
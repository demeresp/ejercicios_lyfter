from sum_average_conversion import divide
import pytest

def test_verifty_5_2_returns_5_0_():
    result = divide(10, 2)
    assert result == 5.0


def test_verify_if_zero_return_Value_Error():
    with pytest.raises(ValueError):
        divide(0,0)


def test_if_divide_with_string_Type_Error():
    with pytest.raises(TypeError):
        divide("a", "a")



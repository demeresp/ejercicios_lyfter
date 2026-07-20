
from return_sum_list import my_numbers

def test_len_list_is_the_same_as_the_number_entered():
    assert len(list(range(1, 33 + 1))) == 33 

def test_if_int_is_zero():
    assert my_numbers(0) == 0


def test_only_one_parameter_has_given():
    assert my_numbers(1) == 1


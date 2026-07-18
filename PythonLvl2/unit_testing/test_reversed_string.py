import pytest
from return_ordered_string import turn_word

def test_if_return_is_string():
    result = turn_word("Hello")
    assert isinstance(result, str)


def test_if_word_is_empty():
    empty_input = ""
    result = turn_word(empty_input)
    assert result == ""


def test_if_word_only_has_one_letter():
    single_letter_input = "a"
    result = turn_word(single_letter_input)
    assert result == "a"
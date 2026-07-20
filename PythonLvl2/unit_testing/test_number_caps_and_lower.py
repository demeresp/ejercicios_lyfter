import pytest #result is result from return
from number_caps_lower import lower_upper

def test_to_check_correct_words_are_input():
    result = lower_upper("World", "Cup", "Final")
    expected_words = ["World", "Cup", "Final"]
    for word in expected_words:
        assert word in result


def test_to_check_if_upper_and_lower_are_counted():
    result = lower_upper("World", "Cup", "Final")
    assert "mayusculas" in result
    assert "minusculas" in result


def test_if_lower_and_caps_are_returned():
    result = lower_upper("World", "Cup", "Final")
 
    has_upper = any(word[0].isupper() for word in result)
    assert has_upper

    has_lower = any(word[0].islower() for word in result)
    assert has_lower
import pytest
from separated_hyphen import my_wordzz

def test_if_output_returns_string():
    result = my_wordzz("This", "is", "JOHN CENA!")
    assert isinstance(result, str)
    

def test_if_words_are_sorted():
    result = my_wordzz("This", "is", "JOHN CENA!")
    expected = sorted(["This", "is", "JOHN CENA!"])
    assert result == " - ".join(expected)


def test_if_returns_words_with_hyphen():
    result = my_wordzz("This", "is", "JOHN CENA!")
    expected = sorted(["This", "is", "JOHN CENA!"])
    assert " - ".join(expected) == result
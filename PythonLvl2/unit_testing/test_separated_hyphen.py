import pytest
from separated_hyphen import my_wordzz

def test_if_inputs_are_strings():
    with pytest.raises(TypeError):
        my_wordzz(12345, 12345, 12345)

    with pytest.raises(TypeError):
        my_wordzz([],[],[])

    with pytest.raises(TypeError):
        my_wordzz({"key":"value"},{"key":"value"},{"key":"value"})
    

def test_if_parameteres_are_empty():
    with pytest.raises(TypeError):
        my_wordzz(None, None, None)


def test_if_returns_words_with_hyphen():
    result = my_wordzz("This", "is", "JOHN CENA!")
    expected = sorted(["This", "is", "JOHN CENA!"])
    assert " - ".join(expected) == result
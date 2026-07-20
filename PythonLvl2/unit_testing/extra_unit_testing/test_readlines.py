from readlines import read_lines
import pytest
from unittest.mock import mock_open, patch #importat unittest y mock que simular comportamiento de cosas y crear objetos falsos

# https://docs.python.org/3/library/unittest.mock.html

def test_if_returns_the_expected_lines_and_do_not_create_anthr_file():
    fake_content = "line1\nline2\nline3\n" #string que simula una ruta
    with patch('builtins.open', mock_open(read_data=fake_content)): #with patch hara que python simule abrir un archivo
        result = read_lines("any_file.txt")                          #builtins contiene todas las funciones de python y al juntarlo con .open confirmaremos reemplazar open
        assert result == ["line1\n", "line2\n", "line3\n"]       #asi no intentara abrir una ruta realmente
                                                                    


def test_if_test_raises_file_not_found_error():
    with patch("builtins.open", side_effect=FileNotFoundError): #side_effect simulara el error que se le de
        with pytest.raises(FileNotFoundError):
            read_lines("any_file.txt")

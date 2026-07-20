import pytest
from math_operations import mysum, averge, convert_to_farenheit

class TestMathOperations:

    def test_positive_numbers(self):
        assert mysum(3, 5) 
        assert averge([1, 2, 3]) == 2.0
        assert convert_to_farenheit(0) == 32


    def test_negative_numbers(self):
        assert mysum(-3, -5) == -8
        assert averge([-1,-2,-3]) == -2.0


    def test_zeros(self):
        assert mysum(0, 0) == 0
        assert averge([0, 0, 0]) == 0
        assert convert_to_farenheit(0) == 32
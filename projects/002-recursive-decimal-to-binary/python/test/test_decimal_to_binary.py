import pytest
import sys
import os

sys.path.append(os.path.abspath("projects/002-recursive-decimal-to-binary"))
from python.main import decimal_to_binary


def test_decimal_to_binary_ok():

    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(11) == "1011"
    assert decimal_to_binary(15) == "1111"


def test_recursive_base_cases():
    assert decimal_to_binary(0) == "0"
    assert decimal_to_binary(1) == "1"


def test_large_number():
    assert decimal_to_binary(1023) == "1111111111"
    assert decimal_to_binary(2**20) == "1" + "0" * 20
    

def test_error_raises():

    with pytest.raises(TypeError):

        decimal_to_binary("Not positive integer")
        decimal_to_binary(1.5)
        decimal_to_binary([])
    
    with pytest.raises(ValueError):

        decimal_to_binary(-10)


if __name__ == "__main__":
    pytest.main()
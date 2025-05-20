import pytest 
import os
import sys

sys.path.append(os.path.abspath("projects/001-total-the-values"))
print(sys.path)
from python.main import total_the_values


def test_sum_of_values():

    """Checks correct summation of numeric values in a list."""

    assert total_the_values([1, 2, 3]) == 6.0
    assert total_the_values([0, 0, 0]) == 0.0
    assert total_the_values([]) == 0.0
    assert total_the_values([1.5, 2.5, 3.0]) == 7.0
    assert total_the_values([-1, -2, 3]) == 0.0

def test_non_list_input():

    """Checks that a TypeError is raised for non-list input."""

    with pytest.raises(TypeError):
        total_the_values("123")

    with pytest.raises(TypeError):
        total_the_values(None)

    with pytest.raises(TypeError):
        total_the_values(123)


def test_non_numeric_in_list():

    """Checks that a TypeError is raised if list contains non-numeric values."""
    
    with pytest.raises(TypeError):
        total_the_values([1, "a", 3])


if __name__ == "__main__":
    pytest.main()
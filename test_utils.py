"""Test module for utils module functions"""

import pytest
import utils


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)])
def test_add(a, b, expected):
    """Test the add function"""
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    """Test the subtract function"""
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    """Test the multiply function"""
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    """Test the divide function"""
    result = utils.divide(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "n, expected", [(0, "0"), (5, "101"), (10, "1010"), (100, "1100100")]
)
def test_decimal_to_binary_correct(n, expected):
    """Test the decimal_to_binary function"""
    result = utils.decimal_to_binary(n)
    assert result == expected


@pytest.mark.parametrize("n", [-1, 101])
def test_decimal_to_binary_out_of_range(n):
    """Test the range of the function"""
    with pytest.raises(ValueError, match="Liczba musi być z zakresu od 0 do 100"):
        utils.decimal_to_binary(n)


@pytest.mark.parametrize("n", [2.5, 3.14])
def test_decimal_to_binary_not_natural(n):
    """Test if the number is natural"""
    with pytest.raises(ValueError, match="Liczba musi być naturalna"):
        utils.decimal_to_binary(n)

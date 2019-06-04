# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""
import pytest
from prime import generate_prime_factors

def test_invalid_input():
    """
    Given non-integer, a ValueError should be raised.
    """
    with pytest.raises(ValueError):
        generate_prime_factors('edward')

def test_input_1():
    """
    Given an input of 1 an empty list should be returned.
    """
    assert generate_prime_factors(1) == []

def test_input_2():
    """
    Given an input of 2 a prime factir of 2 should be returned.
    """
    assert generate_prime_factors(2) == [2]

def test_input_3():
    """
    Given an input of 3 a prime factor of 3 should be returned.
    """
    assert generate_prime_factors(3) == [3]

def test_input_4():
    """
    Given an input of 4 all contributing prime factors, i.e. 2 * 2
    """
    assert generate_prime_factors(4) == [2, 2]

def test_input_6():
    """
    Given an input of 6 all contributing prime factors, i.e. 2 * 3
    this is an example of the orginal requirement to solve at the beginning
    of the assignment (solved for this from the beginning, exludes 1
    prime factor)
    """
    assert generate_prime_factors(6) == [2, 3]

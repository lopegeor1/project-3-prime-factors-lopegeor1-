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

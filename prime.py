"""
prime.py -- Write the application code here
"""
def prime_factors(number):
    """
    Determines all prime factors of a given 'number'.
    """
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors

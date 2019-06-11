"""
prime.py -- Write the application code here
"""
def generate_prime_factors(number):
    """
    Determines all prime factors of a given 'number'.
    """
    i = 2
    factors = []

    #checks if number is an integer, if not raises ValueError
    if not isinstance(number, int):
        raise ValueError

    #checks range of values such that the root squared is not greater
    #than the given number using while loop
    while i * i <= number:
        if number % i: #append
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors

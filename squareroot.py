import math

def square_root(num):
    """
    Returns the square root of a number.
    """
    if num < 0:
        raise ValueError("Square root of a negative number is not defined in real numbers.")
    return math.sqrt(num)

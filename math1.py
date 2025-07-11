import math
def calculate_square_root(number):
    """Calculate the square root of a number."""
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(number)
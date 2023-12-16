from math import sqrt


def gcd(a: int, b: int) -> int:
    """Returns greatest common divisor of two given numbers."""
    while b != 0:
        a, b = b, a % b
    return a


def is_prime(number):
    if number < 2:
        return False
    for divider in range(2, int(sqrt(number)) + 1):
        if not number % divider:
            return False
    return True

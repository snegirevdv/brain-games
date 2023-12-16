def gcd(a: int, b: int) -> int:
    """Returns greatest common divisor of two given numbers."""
    while b != 0:
        a, b = b, a % b
    return a

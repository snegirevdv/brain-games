from random import randint

from brain_games.settings import LIMITS


def get_gcd_data() -> tuple[str]:
    """
    GCD handler. Returns question and correct answer.
    """
    # Get randon numbers
    number1: int = randint(*LIMITS)
    number2: int = randint(*LIMITS)

    question = f"{number1} {number2}"
    correct = str(gcd(number1, number2))
    return question, correct


def gcd(a: int, b: int) -> int:
    """Returns greatest common divisor of two given numbers."""
    while b != 0:
        a, b = b, a % b
    return a

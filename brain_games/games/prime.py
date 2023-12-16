from math import sqrt
from random import randint

from brain_games.settings import LIMITS


def get_prime_data() -> tuple[str]:
    """
    Prime handler. Returns question and correct answer.
    """
    # Get random number
    number: int = randint(*LIMITS)

    correct: str = "yes" if is_prime(number) else "no"
    question = str(number)
    return question, correct


def is_prime(number: int) -> bool:
    """Check if number is prime."""
    if number < 2:
        return False
    for divider in range(2, int(sqrt(number)) + 1):
        if not number % divider:
            return False
    return True

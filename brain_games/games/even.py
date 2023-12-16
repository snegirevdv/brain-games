from random import randint

from brain_games.settings import LIMITS

EVEN_DIVIDER = 2
"""The number with which the estimated number is compared."""


def get_even_data() -> tuple[str]:
    """
    Is even handler. Returns question and correct answer.
    """
    # Get random number
    number: int = randint(*LIMITS)

    # Check if number is even
    is_even: bool = not number % EVEN_DIVIDER

    question = str(number)
    correct: str = "yes" if is_even else "no"
    return question, correct

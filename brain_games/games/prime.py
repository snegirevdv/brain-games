from math import sqrt
from random import randint

from brain_games.settings import LIMITS


def get_data() -> tuple[str]:
    number = randint(*LIMITS)
    correct = "yes" if is_prime(number) else "no"
    question = str(number)
    return question, correct


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for divider in range(2, int(sqrt(number)) + 1):
        if not number % divider:
            return False
    return True

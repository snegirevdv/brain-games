from random import randint

from brain_games import settings


def get_data() -> tuple[str]:
    number = randint(*settings.LIMITS)
    is_even: bool = not number % 2
    question = str(number)
    correct = "yes" if is_even else "no"
    return question, correct

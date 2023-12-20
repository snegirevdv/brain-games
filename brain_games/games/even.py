from random import randint

from brain_games import settings


def get_data() -> tuple[str]:
    number = randint(*settings.NUMBER_LIMITS)
    is_even: bool = not number % 2
    question = str(number)
    correct_answer = "yes" if is_even else "no"
    return question, correct_answer


RULES = ("Answer \"yes\" if the number is even, otherwise answer \"no\".")

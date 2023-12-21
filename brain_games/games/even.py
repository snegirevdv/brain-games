import random

from brain_games import settings


def make_question_answer() -> tuple[str]:
    number = random.randint(*settings.NUMBER_LIMITS)
    is_even: bool = not number % 2
    question = str(number)
    correct_answer = "yes" if is_even else "no"
    return question, correct_answer

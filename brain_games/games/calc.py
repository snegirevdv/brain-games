import random
from typing import Callable

from brain_games import settings, consts


def make_question_answer() -> tuple[str]:
    number1 = random.randint(*settings.NUMBER_LIMITS)
    number2 = random.randint(*settings.NUMBER_LIMITS)
    sign: str = random.choice(tuple(consts.OPERATIONS))
    operation: Callable = consts.OPERATIONS[sign]
    question = f"{number1} {sign} {number2}"
    correct_answer = str(operation(number1, number2))
    return question, correct_answer

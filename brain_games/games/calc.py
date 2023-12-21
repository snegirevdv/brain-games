import operator
import random
from typing import Callable

from brain_games import game

RULES = "What is the result of the expression?"

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}


def make_question_answer() -> tuple[str]:
    number1 = random.randint(*game.NUMBER_LIMITS)
    number2 = random.randint(*game.NUMBER_LIMITS)
    sign: str = random.choice(tuple(OPERATIONS))
    operation: Callable = OPERATIONS[sign]
    question = f"{number1} {sign} {number2}"
    correct_answer = str(operation(number1, number2))
    return question, correct_answer

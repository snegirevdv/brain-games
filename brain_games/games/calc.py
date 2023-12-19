import operator
import random
from typing import Callable

from brain_games import settings

OPERATIONS: dict[str, Callable] = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}

def get_data() -> tuple[str]:
    number1 = random.randint(*settings.LIMITS)
    number2 = random.randint(*settings.LIMITS)
    sign: str = random.choice(list(OPERATIONS.keys()))
    operation: Callable = OPERATIONS[sign]
    question = f"{number1} {sign} {number2}"
    correct = str(operation(number1, number2))
    return question, correct

from operator import add, sub, mul
from random import choice, randint
from typing import Callable

from brain_games.settings import LIMITS

OPERATIONS: dict[str, Callable] = {
    "+": add,
    "-": sub,
    "*": mul,
}
"""Dictionary of ariphmetic functions."""


def get_calc_data() -> tuple[str]:
    """
    Calculator handler. Returns question and correct answer.
    """
    # Get random numbers
    number1: int = randint(*LIMITS)
    number2: int = randint(*LIMITS)

    # Get sign and function from dict
    sign: str = choice(list(OPERATIONS.keys()))
    operation: Callable = OPERATIONS[sign]

    question = f"{number1} {sign} {number2}"
    correct = str(operation(number1, number2))
    return question, correct

from random import choice, randint
from typing import Callable

from brain_games.logic.settings import EVEN_DELIMETER, LIMITS, OPERATIONS
from brain_games.logic.utils import gcd


def get_even_data():
    """
    Is even handler.
    Returns question and correct answer.
    """
    number: int = randint(*LIMITS)
    question = str(number)
    correct: str = "yes" if not number % EVEN_DELIMETER else "no"
    return question, correct


def get_calc_data():
    """
    Calculator handler.
    Returns question and correct answer.
    """
    number1: int = randint(*LIMITS)
    number2: int = randint(*LIMITS)
    sign: str = choice(list(OPERATIONS.keys()))
    operation: Callable = OPERATIONS[sign]
    question = f"{number1} {sign} {number2}"
    correct = str(operation(number1, number2))
    return question, correct


def get_gcd_data():
    """
    GCD handler.
    Returns question and correct answer.
    """
    number1: int = randint(*LIMITS)
    number2: int = randint(*LIMITS)
    question = f"{number1} {number2}"
    correct = str(gcd(number1, number2))
    return question, correct


GAME_HANDLERS: dict[str, Callable] = {
    "even": get_even_data,
    "calc": get_calc_data,
    "gcd": get_gcd_data,
}
"""Handlers list."""

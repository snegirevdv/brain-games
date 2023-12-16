from random import choice, randint
from typing import Callable

from brain_games.logic.settings import (EVEN_DELIMETER, LEN_LIMITS, LIMITS,
                                        OPERATIONS, STEP_LIMITS)
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


def get_progression_data():
    """
    Progression handler.
    Returns question and correct answer.
    """
    length: int = randint(*LEN_LIMITS)
    start: int = randint(*LIMITS)
    step: int = randint(*STEP_LIMITS)
    stop: int = start + length * step + 1
    progression: list[str] = list(map(str, range(start, stop, step)))
    hiden_index: int = choice(range(length))
    correct = progression[hiden_index]
    progression[hiden_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct


GAME_HANDLERS: dict[str, Callable] = {
    "even": get_even_data,
    "calc": get_calc_data,
    "gcd": get_gcd_data,
    "progression": get_progression_data,
}
"""Handlers list."""

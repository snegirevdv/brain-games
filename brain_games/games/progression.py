from random import choice, randint

from brain_games.settings import LIMITS

LEN_LIMITS: tuple[int] = (5, 10)
"""Limits for len of progression."""
SIGNS: tuple[int] = (-1, 1)
"""Signs of numbers. -1 - negative, 1 - positive."""


def get_progression_data() -> tuple[str]:
    """
    Progression handler.
    Returns question and correct answer.
    """
    # Get progression
    length: int = randint(*LEN_LIMITS)
    start: int = randint(*LIMITS)
    step: int = randint(*LIMITS) * choice(SIGNS)
    stop: int = start + length * step + 1
    progression: list[str] = list(map(str, range(start, stop, step)))

    # Hide random element
    hiden_index: int = choice(range(length))
    correct = progression[hiden_index]
    progression[hiden_index] = ".."

    question = " ".join(map(str, progression))
    return question, correct

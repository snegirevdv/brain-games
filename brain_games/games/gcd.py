from random import randint

from brain_games.settings import LIMITS


def get_gcd_data() -> tuple[str]:
    number1: int = randint(*LIMITS)
    number2: int = randint(*LIMITS)
    question = f"{number1} {number2}"
    correct = str(gcd(number1, number2))
    return question, correct


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

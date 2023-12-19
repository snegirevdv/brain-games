from random import randint

from brain_games import settings


def get_data() -> tuple[str]:
    number1 = randint(*settings.LIMITS)
    number2 = randint(*settings.LIMITS)
    question = f"{number1} {number2}"
    correct = str(gcd(number1, number2))
    return question, correct


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

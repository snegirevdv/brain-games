from random import randint

from brain_games import settings


def get_data() -> tuple[str]:
    number1 = randint(*settings.NUMBER_LIMITS)
    number2 = randint(*settings.NUMBER_LIMITS)
    question = f"{number1} {number2}"
    correct_answer = str(gcd(number1, number2))
    return question, correct_answer


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

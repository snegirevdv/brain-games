from random import randint

from brain_games import settings


def gen_question_answer() -> tuple[str]:
    number1 = randint(*settings.NUMBER_LIMITS)
    number2 = randint(*settings.NUMBER_LIMITS)
    question = f"{number1} {number2}"
    correct_answer = str(calc_gcd(number1, number2))
    return question, correct_answer


def calc_gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


RULES = "Find the greatest common divisor of given numbers."

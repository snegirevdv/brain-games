import random

from brain_games import game

RULES = "Find the greatest common divisor of given numbers."


def make_question_answer() -> tuple[str]:
    number1 = random.randint(*game.NUMBER_LIMITS)
    number2 = random.randint(*game.NUMBER_LIMITS)
    question = f"{number1} {number2}"
    correct_answer = str(find_gcd(number1, number2))
    return question, correct_answer


def find_gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

import math
import random

from brain_games import settings


def get_data() -> tuple[str]:
    number = random.randint(*settings.NUMBER_LIMITS)
    correct_answer = "yes" if is_prime(number) else "no"
    question = str(number)
    return question, correct_answer


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for divider in range(2, int(math.sqrt(number)) + 1):
        if not number % divider:
            return False
    return True

from random import randint

from brain_games.settings import LIMITS

def get_even_data() -> tuple[str]:
    number: int = randint(*LIMITS)
    is_even: bool = not number % 2
    question = str(number)
    correct: str = "yes" if is_even else "no"
    return question, correct

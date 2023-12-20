import random

from brain_games import settings


def generate_progression(length: int) -> list[str]:
    start = random.randint(*settings.NUMBER_LIMITS)
    step_abs = random.randint(*settings.PROGRESSION_STEP_LIMITS)
    step_sign = random.choice(settings.NUMERIC_SIGNS)
    step: int = step_abs * step_sign
    stop: int = start + length * step + 1
    return list(map(str, range(start, stop, step)))


def get_data() -> tuple[str]:
    length = random.randint(*settings.PROGRESSION_LEN_LIMITS)
    progression = generate_progression(length)
    hiden_index: int = random.choice(range(length))
    correct_answer = progression[hiden_index]
    progression[hiden_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer

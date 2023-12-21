import random

from brain_games import settings


def make_question_answer() -> tuple[str]:
    length = random.randint(*settings.PROGRESSION_LEN_LIMITS)
    progression = make_progression(length)
    hiden_index: int = random.choice(range(length))
    correct_answer = progression[hiden_index]
    progression[hiden_index] = ".."
    question = " ".join(progression)
    return question, correct_answer


def make_progression(length: int) -> list[str]:
    start = random.randint(*settings.NUMBER_LIMITS)
    step_abs = random.randint(*settings.PROGRESSION_STEP_LIMITS)
    step_sign = random.choice(settings.NUMERIC_SIGNS)
    step: int = step_abs * step_sign
    stop: int = start + length * step + 1
    return [str(number) for number in range(start, stop, step)]

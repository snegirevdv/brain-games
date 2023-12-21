import random

from brain_games import game

PROGRESSION_LEN_LIMITS = (5, 10)
PROGRESSION_STEP_LIMITS = (1, 50)
NUMERIC_SIGNS = (-1, 1)

RULES = "What number is missing in the progression?"


def make_progression(length: int) -> list[str]:
    start = random.randint(*game.NUMBER_LIMITS)
    step_abs = random.randint(*PROGRESSION_STEP_LIMITS)
    step_sign = random.choice(NUMERIC_SIGNS)
    step: int = step_abs * step_sign
    stop: int = start + length * step + 1
    return [str(number) for number in range(start, stop, step)]


def make_question_answer() -> tuple[str]:
    length = random.randint(*PROGRESSION_LEN_LIMITS)
    progression = make_progression(length)
    hiden_index: int = random.choice(range(length))
    correct_answer = progression[hiden_index]
    progression[hiden_index] = ".."
    question = " ".join(progression)
    return question, correct_answer

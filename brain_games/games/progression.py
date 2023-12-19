import random

from brain_games import settings


def generate_progression(length: int) -> list[str]:
    start = random.randint(*settings.LIMITS)
    step = random.randint(*settings.LIMITS) * random.choice(settings.SIGNS)
    stop: int = start + length * step + 1
    return list(map(str, range(start, stop, step)))


def get_data() -> tuple[str]:
    length = random.randint(*settings.LEN_LIMITS)
    progression = generate_progression(length)
    hiden_index: int = random.choice(range(length))
    correct = progression[hiden_index]
    progression[hiden_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct

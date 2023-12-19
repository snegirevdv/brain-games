from random import choice, randint

from brain_games.settings import LIMITS, LEN_LIMITS, SIGNS


def get_data() -> tuple[str]:
    # Get progression
    length = randint(*LEN_LIMITS)
    start = randint(*LIMITS)
    step = randint(*LIMITS) * choice(SIGNS)
    stop: int = start + length * step + 1
    progression: list[str] = list(map(str, range(start, stop, step)))

    # Hide random element
    hiden_index: int = choice(range(length))
    correct = progression[hiden_index]
    progression[hiden_index] = ".."

    question = " ".join(map(str, progression))
    return question, correct

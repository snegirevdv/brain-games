from enum import Enum, auto
from typing import Callable

from brain_games.games import calc, even, gcd, prime, progression


class Handler(Enum):
    EVEN = auto()
    CALC = auto()
    GCD = auto()
    PROGRESSION = auto()
    PRIME = auto()

    def get_data(self) -> Callable:
        return DATA_FUNCTIONS[self]

    def get_rules(self) -> str:
        return RULES[self]


DATA_FUNCTIONS: dict[Handler, Callable] = {
    Handler.EVEN: even.get_data,
    Handler.CALC: calc.get_data,
    Handler.GCD: gcd.get_data,
    Handler.PROGRESSION: progression.get_data,
    Handler.PRIME: prime.get_data,
}

RULES: dict[Handler, str] = {
    Handler.EVEN: even.RULES,
    Handler.CALC: calc.RULES,
    Handler.GCD: gcd.RULES,
    Handler.PROGRESSION: progression.RULES,
    Handler.PRIME: prime.RULES,
}

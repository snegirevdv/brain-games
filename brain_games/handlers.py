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
    Handler.EVEN: ("Answer \"yes\" if the number is even, "
                   "otherwise answer \"no\"."),
    Handler.CALC: "What is the result of the expression?",
    Handler.GCD: "Find the greatest common divisor of given numbers.",
    Handler.PROGRESSION: "What number is missing in the progression?",
    Handler.PRIME: ("Answer \"yes\" if given number is prime. "
                    "Otherwise answer \"no\"."),
}

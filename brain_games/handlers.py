from enum import Enum
from typing import Callable

from brain_games.games import calc, even, gcd, prime, progression


class Handler(Enum):
    EVEN = "even"
    CALC = "calc"
    GCD = "gcd"
    PROGRESSION = "progression"
    PRIME = "prime"

    def get_data(self) -> Callable:
        return DATA[self]

    def get_rules(self) -> str:
        return RULES[self]


DATA: dict[str, Callable] = {
    Handler.EVEN: even.get_data,
    Handler.CALC: calc.get_data,
    Handler.GCD: gcd.get_data,
    Handler.PROGRESSION: progression.get_data,
    Handler.PRIME: prime.get_data,
}

RULES: dict[str, str] = {
    Handler.EVEN: ("Answer \"yes\" if the number is even, "
                   "otherwise answer \"no\"."),
    Handler.CALC: "What is the result of the expression?",
    Handler.GCD: "Find the greatest common divisor of given numbers.",
    Handler.PROGRESSION: "What number is missing in the progression?",
    Handler.PRIME: ("Answer \"yes\" if given number is prime. "
                    "Otherwise answer \"no\"."),
}
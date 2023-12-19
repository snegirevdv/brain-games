from enum import Enum
from typing import Callable

from brain_games.games import calc, even, gcd, prime, progression
from brain_games.messages import (CALC_RULES, EVEN_RULES, GCD_RULES,
                                            PRIME_RULES, PROGRESSION_RULES)


class Handler(Enum):
    EVEN = "even"
    CALC = "calc"
    GCD = "gcd"
    PROGRESSION = "progression"
    PRIME = "prime"

    def get_function(self) -> Callable:
        return FUNCTIONS[self]

    def get_rules(self) -> str:
        return RULES[self]


FUNCTIONS: dict[str, Callable] = {
    Handler.EVEN: even.get_data,
    Handler.CALC: calc.get_data,
    Handler.GCD: gcd.get_data,
    Handler.PROGRESSION: progression.get_data,
    Handler.PRIME: prime.get_data,
}

RULES: dict[str, str] = {
    Handler.EVEN: EVEN_RULES,
    Handler.CALC: CALC_RULES,
    Handler.GCD: GCD_RULES,
    Handler.PROGRESSION: PROGRESSION_RULES,
    Handler.PRIME: PRIME_RULES,
}

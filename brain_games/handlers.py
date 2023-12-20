from enum import Enum
from typing import Callable

from brain_games.games import calc, even, gcd, prime, progression


class Handler(Enum):
    EVEN = "even"
    CALC = "calc"
    GCD = "gcd"
    PROGRESSION = "progression"
    PRIME = "prime"


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

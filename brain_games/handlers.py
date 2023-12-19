from enum import Enum
from typing import Callable

from brain_games.games.calc import get_calc_data
from brain_games.games.even import get_even_data
from brain_games.games.gcd import get_gcd_data
from brain_games.games.prime import get_prime_data
from brain_games.games.progression import get_progression_data
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
    Handler.EVEN: get_even_data,
    Handler.CALC: get_calc_data,
    Handler.GCD: get_gcd_data,
    Handler.PROGRESSION: get_progression_data,
    Handler.PRIME: get_prime_data,
}

RULES: dict[str, str] = {
    Handler.EVEN: EVEN_RULES,
    Handler.CALC: CALC_RULES,
    Handler.GCD: GCD_RULES,
    Handler.PROGRESSION: PROGRESSION_RULES,
    Handler.PRIME: PRIME_RULES,
}

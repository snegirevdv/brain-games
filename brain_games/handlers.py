from enum import Enum
from typing import Callable

from brain_games.games import calc, even, gcd, prime, progression


class Handler(Enum):
    EVEN = "even"
    CALC = "calc"
    GCD = "gcd"
    PROGRESSION = "progression"
    PRIME = "prime"


GEN_QNA_FUNCTIONS: dict[Handler, Callable] = {
    Handler.EVEN: even.gen_question_answer,
    Handler.CALC: calc.gen_question_answer,
    Handler.GCD: gcd.gen_question_answer,
    Handler.PROGRESSION: progression.gen_question_answer,
    Handler.PRIME: prime.gen_question_answer,
}

RULES: dict[Handler, str] = {
    Handler.EVEN: even.RULES,
    Handler.CALC: calc.RULES,
    Handler.GCD: gcd.RULES,
    Handler.PROGRESSION: progression.RULES,
    Handler.PRIME: prime.RULES,
}

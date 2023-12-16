from typing import Callable

from brain_games.games.calc import get_calc_data
from brain_games.games.even import get_even_data
from brain_games.games.gcd import get_gcd_data
from brain_games.games.prime import get_prime_data
from brain_games.games.progression import get_progression_data


# Game Handlers
GAME_HANDLERS: dict[str, Callable] = {
    "even": get_even_data,
    "calc": get_calc_data,
    "gcd": get_gcd_data,
    "progression": get_progression_data,
    "prime": get_prime_data,
}
"""Handlers list."""

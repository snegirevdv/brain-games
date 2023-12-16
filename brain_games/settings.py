from operator import add, sub, mul
from typing import Callable

# General settings
ROUNDS = 3
"""Amount of rounds in the game."""
LIMITS: tuple[int] = (1, 25)
"""Tuple of minimal and maximal random number."""

# Even
EVEN_DELIMETER = 2
"""The number with which the estimated number is compared."""

# Calculator
OPERATIONS: dict[str, Callable] = {
    "+": add,
    "-": sub,
    "*": mul,
}
"""Dictionary of ariphmetic functions."""

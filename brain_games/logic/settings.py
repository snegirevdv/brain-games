from operator import add, sub, mul
from typing import Callable

# General settings
ROUNDS = 3
"""Amount of rounds in the game."""
LIMITS: tuple[int] = (1, 100)
"""Tuple of minimal and maximal random number."""

# Even
EVEN_DIVIDER = 2
"""The number with which the estimated number is compared."""

# Calculator
OPERATIONS: dict[str, Callable] = {
    "+": add,
    "-": sub,
    "*": mul,
}
"""Dictionary of ariphmetic functions."""

# Progression
LEN_LIMITS: tuple[int] = (5, 10)
"""Limits for len of progression."""
STEP_LIMITS: tuple[int] = (-10, 10)
"""Limits of step of progression."""

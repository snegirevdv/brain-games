#!/usr/bin/env_python3
from brain_games.cli.cli import welcome_user
from brain_games.cli.game_controller import start_game


def main() -> None:
    """Run Calc game"""
    username: str = welcome_user()
    start_game(username=username, game="calc")


if __name__ == "__main__":
    main()

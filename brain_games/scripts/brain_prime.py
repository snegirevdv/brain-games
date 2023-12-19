#!/usr/bin/env_python3
from brain_games.cli.cli import welcome_user
from brain_games.cli.game_controller import start_game
from brain_games.handlers import Handler


def main() -> None:
    username: str = welcome_user()
    start_game(username=username, game=Handler.PRIME)


if __name__ == "__main__":
    main()

#!/usr/bin/env_python3
from brain_games import cli
from brain_games.handlers import Handler


def main() -> None:
    username: str = cli.welcome_user()
    cli.start_game(username=username, game=Handler.PROGRESSION)


if __name__ == "__main__":
    main()

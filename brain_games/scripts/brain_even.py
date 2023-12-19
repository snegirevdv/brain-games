#!/usr/bin/env_python3
from brain_games.cli import cli, game_controller
from brain_games.handlers import Handler


def main() -> None:
    username: str = cli.welcome_user()
    game_controller.start_game(username=username, game=Handler.EVEN)


if __name__ == "__main__":
    main()

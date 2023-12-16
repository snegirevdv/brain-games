#!/usr/bin/env_python3
from brain_games.cli.cli import welcome_user
from brain_games.cli.game import start_game


def main():
    username = welcome_user()
    start_game(username=username, game="calc")


if __name__ == "__main__":
    main()

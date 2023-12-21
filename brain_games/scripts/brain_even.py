#!/usr/bin/env_python3
from brain_games import cli
from brain_games import game
from brain_games.games import even


def main() -> None:
    username: str = cli.welcome_user()
    game.start_game(username, even.make_question_answer, even.RULES)


if __name__ == "__main__":
    main()

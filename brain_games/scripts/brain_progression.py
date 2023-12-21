#!/usr/bin/env_python3
from brain_games import cli
from brain_games import game
from brain_games.games import progression


def main() -> None:
    username: str = cli.welcome_user()
    game.start_game(username,
                    progression.make_question_answer,
                    progression.RULES)


if __name__ == "__main__":
    main()

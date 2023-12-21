#!/usr/bin/env python3

from brain_games import cli, game, consts
from brain_games.games import calc


def main() -> None:
    username: str = cli.welcome_user()
    game.start_game(username, calc.make_question_answer, consts.CALC_RULES)


if __name__ == "__main__":
    main()

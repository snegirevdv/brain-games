#!/usr/bin/env python3

from brain_games import cli, game, consts
from brain_games.games import gcd


def main() -> None:
    username: str = cli.welcome_user()
    game.start_game(username, gcd.make_question_answer, consts.GCD_RULES)


if __name__ == "__main__":
    main()

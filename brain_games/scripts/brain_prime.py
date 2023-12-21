#!/usr/bin/env python3

from brain_games import cli, game, consts
from brain_games.games import prime


def main() -> None:
    username: str = cli.welcome_user()
    game.start_game(username, prime.make_question_answer, consts.PRIME_RULES)


if __name__ == "__main__":
    main()

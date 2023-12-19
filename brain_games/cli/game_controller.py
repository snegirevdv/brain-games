from prompt import string

from brain_games.handlers import Handler
from brain_games.settings import ROUNDS
from brain_games.messages import (CONGRATULATION, CORRECT, LOSE,
                                            QUESTION, USER_ANSWER)


def start_game(username: str, game: Handler) -> None:
    print(game.get_rules())
    for _ in range(ROUNDS):
        question, correct = game.get_function()()
        print(QUESTION.format(question))
        answer: str = string(USER_ANSWER)
        if answer == correct:
            print(CORRECT)
        else:
            print(LOSE.format(answer, correct, username))
            break
    else:
        print(CONGRATULATION.format(username))

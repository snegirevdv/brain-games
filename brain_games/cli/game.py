from prompt import string

from brain_games.logic.handlers import GAME_HANDLERS
from brain_games.logic.settings import ROUNDS
from brain_games.locale.messages_en import (CONGRATULATION, CORRECT, LOSE,
                                            RULES, QUESTION, USER_ANSWER)


def start_game(username, game):
    """
    Starts game and controls game process.
    """
    print(RULES[game])
    for _ in range(ROUNDS):
        question, correct = GAME_HANDLERS[game]()
        print(QUESTION.format(question))
        answer = string(USER_ANSWER)
        if answer == correct:
            print(CORRECT)
        else:
            print(LOSE.format(answer, correct, username))
            break
    else:
        print(CONGRATULATION.format(username))

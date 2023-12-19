from prompt import string

from brain_games.handlers import Handler
from brain_games.settings import ROUNDS
from brain_games.locale.messages_en import (CONGRATULATION, CORRECT, LOSE,
                                            QUESTION, USER_ANSWER)


def start_game(username: str, game: Handler) -> None:
    """
    Starts game and controls game process.
    """
    print(game.get_rules())

    for _ in range(ROUNDS):
        # Get question body and correct answer from handler
        question, correct = game.get_function()()

        # Get user's answer
        print(QUESTION.format(question))
        answer: str = string(USER_ANSWER)

        if answer == correct:
            print(CORRECT)
        else:
            print(LOSE.format(answer, correct, username))
            break
    else:
        # Print final winning message
        print(CONGRATULATION.format(username))

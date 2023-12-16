from prompt import string

from brain_games.handlers import GAME_HANDLERS
from brain_games.settings import ROUNDS
from brain_games.locale.messages_en import (CONGRATULATION, CORRECT, LOSE,
                                            RULES, QUESTION, USER_ANSWER)


def start_game(username: str, game: str) -> None:
    """
    Starts game and controls game process.
    """
    print(RULES[game])

    for _ in range(ROUNDS):
        # Get question body and correct answer from handler
        question, correct = GAME_HANDLERS[game]()

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

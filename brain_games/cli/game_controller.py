import prompt

from brain_games import handlers
from brain_games import settings


def start_game(username: str, game: handlers.Handler) -> None:
    print(game.get_rules())
    for _ in range(settings.ROUNDS):
        question, correct = game.get_function()()
        print(f"Question: {question}")
        answer: str = prompt.string("Your answer: ")
        if answer == correct:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct}'.\n"
                  f"Let's try again, {username}!")
            break
    else:
        print("Congratulations, {username}!")

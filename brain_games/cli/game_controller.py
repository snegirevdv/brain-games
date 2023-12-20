import prompt

from brain_games import settings
from brain_games.handlers import Handler


def start_game(username: str, game: Handler) -> None:
    print(game.get_rules())
    for _ in range(settings.ROUNDS):
        question, correct = game.get_data()()
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
        print(f"Congratulations, {username}!")

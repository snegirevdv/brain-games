import prompt

from brain_games import settings
from brain_games import handlers


def start_game(username: str, game: handlers.Handler) -> None:
    print(handlers.RULES[game])
    for _ in range(settings.ROUNDS_AMOUNT):
        question, correct_answer = handlers.GEN_QNA_FUNCTIONS[game]()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {username}!")
            break
    else:
        print(f"Congratulations, {username}!")

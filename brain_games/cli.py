import prompt

from brain_games import settings
from brain_games import handlers


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    username = prompt.string("May I have your name? ")
    print(f"Hello, {username}!")
    return username


def start_game(username: str, game: handlers.Handler) -> None:
    gen_question_answer = handlers.QUESTION_ANSWER_MAKERS[game]
    rules = handlers.RULES[game]
    print(rules)
    for _ in range(settings.ROUNDS_AMOUNT):
        question, correct_answer = gen_question_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {username}!")
            return
    else:
        print(f"Congratulations, {username}!")

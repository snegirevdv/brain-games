from typing import Callable
import prompt

from brain_games import settings


def start_game(
        username: str,
        question_answer_maker: Callable,
        rules: str) -> None:
    print(rules)
    for _ in range(settings.ROUNDS_AMOUNT):
        question, correct_answer = question_answer_maker()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {username}!"
            )
            return
    print(f"Congratulations, {username}!")

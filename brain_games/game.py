from typing import Callable as func
import prompt

ROUNDS_AMOUNT = 3
NUMBER_LIMITS = (1, 100)


def start_game(username: str, make_question_answer: func, rules: str) -> None:
    print(rules)
    for _ in range(ROUNDS_AMOUNT):
        question, correct_answer = make_question_answer()
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

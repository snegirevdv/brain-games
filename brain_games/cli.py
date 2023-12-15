from prompt import string


def welcome_user():
    print("Welcome to the Brain Games!")
    username: str = string("May I have your name? ")
    print(f"Hello, {username}!")
    return username

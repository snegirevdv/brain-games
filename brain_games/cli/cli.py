import prompt


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    username = prompt.sting("May I have your name? ")
    print(f"Hello, {username}!")
    return username

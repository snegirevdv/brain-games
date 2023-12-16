from prompt import string
from brain_games.messages_en import WELCOME, ASK_NAME, GREETING


def welcome_user() -> str:
    """
    Prints welcome message and returns username.
    """
    print(WELCOME)
    username = string(ASK_NAME)
    print(GREETING.format(username))
    return username

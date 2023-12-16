from prompt import string
from brain_games.messages import WELCOME, ASK_NAME, GREETING


def welcome_user():
    print(WELCOME)
    username: str = string(ASK_NAME)
    print(GREETING.format(username))
    return username

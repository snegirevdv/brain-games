from random import randint
from prompt import string
from brain_games.constants import (EVEN_DELIMETER,
                                   EVEN_LIMITS, ROUNDS)
from brain_games.messages import (CONGRATULATION, CORRECT, LOSE,
                      RULES, QUESTION, USER_ANSWER)

def get_game_data(game):
    GAME_FUNCTIONS = {
        "even": get_even_data,
    }
    return GAME_FUNCTIONS[game]

def get_even_data():
    number = randint(*EVEN_LIMITS)
    question = str(number)
    correct = "yes" if not number % EVEN_DELIMETER else "no"
    return question, correct
        
def start_game(username, game):
    print(RULES[game])
    for _ in range(ROUNDS):
        question, correct = get_game_data(game)()
        print(QUESTION.format(question))
        answer = string(USER_ANSWER)
        if answer == correct:
            print(CORRECT)
        else:
            print(LOSE.format(answer, correct, username))
            break
    else:
        print(CONGRATULATION.format(username))


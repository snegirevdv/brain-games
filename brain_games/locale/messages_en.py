# Welcome messages
WELCOME = "Welcome to the Brain Games!"
ASK_NAME = "May I have your name? "
GREETING = "Hello, {}!"

# Rules
EVEN_RULES = ("Answer \"yes\" if the number is even, "
              "otherwise answer \"no\".")
CALC_RULES = "What is the result of the expression?"
GCD_RULES = "Find the greatest common divisor of given numbers."
PROGRESSION_RULES = "What number is missing in the progression?"
PRIME_RULES = ("Answer \"yes\" if given number is prime. "
               "Otherwise answer \"no\".")

RULES: dict[str, str] = {
    "even": EVEN_RULES,
    "calc": CALC_RULES,
    "gcd": GCD_RULES,
    "progression": PROGRESSION_RULES,
    "prime": PRIME_RULES,
}

# Ingame messages
QUESTION = "Question: {}"
USER_ANSWER = "Your answer: "
CORRECT = "Correct!"
LOSE = ("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
        "Let's try again, {}!")
CONGRATULATION = "Congratulations, {}!"

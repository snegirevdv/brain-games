# welcome messages
WELCOME = "Welcome to the Brain Games!"
ASK_NAME = "May I have your name? "
GREETING = "Hello, {}!"

# rules
EVEN_RULES = ("Answer \"yes\" if the number is even, "
              "otherwise answer \"no\".")
CALC_RULES = "What is the result of the expression?"
GCD_RULES = "Find the greatest common divisor of given numbers."
RULES: dict[str, str] = {
    "even": EVEN_RULES,
    "calc": CALC_RULES,
    "gcd": GCD_RULES,
}

# game
QUESTION = "Question: {}"
USER_ANSWER = "Your answer: "
CORRECT = "Correct!"
LOSE = ("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
        "Let's try again, {}!")
CONGRATULATION = "Congratulations, {}!"

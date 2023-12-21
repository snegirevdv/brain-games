import operator

# Rules
CALC_RULES = "What is the result of the expression?"
EVEN_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
GCD_RULES = "Find the greatest common divisor of given numbers."
PRIME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
PROGRESSION_RULES = "What number is missing in the progression?"

# Calculator
OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}

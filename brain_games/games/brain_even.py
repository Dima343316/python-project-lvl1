from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_POSSIBLE_NUM = 1
MAX_POSSIBLE_NUM = 99


def is_even(number):
    return number % 2 == 0


def generate_round():
    first_number = randint(MIN_POSSIBLE_NUM, MAX_POSSIBLE_NUM)
    question = first_number
    answer = 'yes' if is_even(question) else 'no'
    return question, answer

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_POSSIBLE_NUM = 1
MAX_POSSIBLE_NUM = 99


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def generate_round():
    first_number = randint(MIN_POSSIBLE_NUM, MAX_POSSIBLE_NUM)
    question = first_number
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer

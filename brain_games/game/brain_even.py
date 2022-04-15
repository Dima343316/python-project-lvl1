import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(number):
    return number % 2 == 0


def generate_round():
    first_random_number = random.randint(0, 101)
    first_random_number_str = str(first_random_number)
    if even(first_random_number) is True:
        return str(first_random_number_str), 'yes'
    else:
        return str(first_random_number_str), 'no'

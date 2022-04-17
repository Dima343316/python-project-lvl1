from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(number):
    return number % 2 == 0


def generate_round():
    min_possible_num = 1
    max_possible_num = 99
    first_number = randint(min_possible_num, max_possible_num)
    first_random_number_str = str(first_number)
    if even(first_number) is True:
        return str(first_random_number_str), 'yes'
    else:
        return str(first_random_number_str), 'no'

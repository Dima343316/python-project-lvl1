import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(number):
    return number % 2 == 0

def generate_param():
        random_number = random.randint(0, 101)
        number = str(random_number)
        if even(random_number) is True:
            return str(number), 'yes'
        else:
            return str(number), 'no'

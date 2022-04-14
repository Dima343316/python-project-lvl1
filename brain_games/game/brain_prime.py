import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    result = {True: 'yes', False: 'no'}
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return result[False]
    return result[True]


def generate_param():
    num = random.randint(2, 100)
    if is_prime(num) is True:
        return str(num), 'yes'
    else:
        return str(num), 'no'

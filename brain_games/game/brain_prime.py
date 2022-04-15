import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


def generate_round():
    first_random_num = random.randint(0, 101)
    if is_prime(first_random_num) is True:
        return str(first_random_num), 'yes'
    else:
        return str(first_random_num), 'no'

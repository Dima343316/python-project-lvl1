from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


def generate_round():
    min_possible_num = 1
    max_possible_num = 99
    first_number = randint(min_possible_num, max_possible_num)
    if is_prime(first_number) is True:
        return str(first_number), 'yes'
    else:
        return str(first_number), 'no'

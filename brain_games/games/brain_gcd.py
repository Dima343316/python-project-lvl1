from math import gcd
from random import randint


DESCRIPTION = "Find the greatest common divisor of given numbers."
MIN_POSSIBLE_NUM = 1
MAX_POSSIBLE_NUM = 99


def generate_round():
    first_number = randint(MIN_POSSIBLE_NUM, MAX_POSSIBLE_NUM)
    second_number = randint(MIN_POSSIBLE_NUM, MAX_POSSIBLE_NUM)
    question = (str(first_number) + ' ' + str(second_number))
    nodes_of_two_numbers = gcd(first_number, second_number)
    return question, str(nodes_of_two_numbers)

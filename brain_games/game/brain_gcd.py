from math import gcd
from random import randint


DESCRIPTION = "Find the greatest common divisor of given numbers."
min_possible_num = 1
max_possible_num = 99
first_number = randint(min_possible_num, max_possible_num)
second_number = randint(min_possible_num, max_possible_num)


def generate_round():
    question = (str(first_number) + ' ' + str(second_number))
    nodes_of_two_numbers = gcd(first_number, second_number)
    return question, str(nodes_of_two_numbers)

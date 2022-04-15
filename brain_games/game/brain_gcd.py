from math import gcd
import random


DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_round():
    first_random_num = random.randint(0, 101)
    second_random_num = random.randint(0, 101)
    question = (str(first_random_num) + ' ' + str(second_random_num))
    nodes_of_two_numbers = gcd(first_random_num, second_random_num)
    return question, str(nodes_of_two_numbers)

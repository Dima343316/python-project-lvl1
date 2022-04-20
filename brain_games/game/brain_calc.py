#!/usr/bin/env python3
import operator
from random import randint
import random


DESCRIPTION = 'What is the result of the expression?'
min_possible_num = 1
max_possible_num = 99
first_number = randint(min_possible_num, max_possible_num)
second_number = randint(min_possible_num, max_possible_num)


def generate_round():
    signs = ['-', '*', '+']
    sign = random.choice(signs)
    expression = (str(first_number) + ' ' + sign + ' ' + str(second_number))
    operations = {'+': operator.add(first_number, second_number),
                  '-': operator.sub(first_number, second_number),
                  '*': operator.mul(first_number, second_number)}
    answer = operations[sign]
    return expression, str(answer)

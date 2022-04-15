#!/usr/bin/env python3
import operator
import random


DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    first_ran_num = (random.randint(0, 101))
    second_ran_num = (random.randint(0, 101))
    signs = ['-', '*', '+']
    sign = random.choice(signs)
    expression = (str(first_ran_num) + ' ' + sign + ' ' + str(second_ran_num))
    operations = {'+': operator.add(first_ran_num, second_ran_num),
                  '-': operator.sub(first_ran_num, second_ran_num),
                  '*': operator.mul(first_ran_num, second_ran_num)}
    answer = operations[sign]
    return expression, str(answer)

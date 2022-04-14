#!/usr/bin/env python3
import operator
import random


DESCRIPTION = 'What is the result of the expression?'


def generate_param():
    random_num = (random.randint(0, 101))
    random_1 = (random.randint(0, 101))
    signs = ['-', '*', '+']
    sin = random.choice(signs)
    num = (str(random_num) + ' ' + sin + ' ' + str(random_1))
    funks = {'+': operator.add(random_num, random_1),
            '-': operator.sub(random_num, random_1),
            '*': operator.mul(random_num, random_1)}
    answer = funks[sin]
    return num, str(answer)

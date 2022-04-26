import operator
from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'
MIN_POSSIBLE_NUM = 1
MAX_POSSIBLE_NUM = 99
OPERATORS = {'+': operator.add, '-': operator.sub,
             '*': operator.mul}


def calc(num1, num2, operation):
    necessary_func = OPERATORS.get(operation)
    return necessary_func(num1, num2)


def generate_round():
    first_num = randint(MIN_POSSIBLE_NUM, MAX_POSSIBLE_NUM)
    second_num = randint(MIN_POSSIBLE_NUM, MAX_POSSIBLE_NUM)
    operation = choice(list(OPERATORS.keys()))
    question = str(first_num) + ' ' + str(operation) + ' ' + str(second_num)
    right_answer = calc(first_num, second_num, operation)
    return question, str(right_answer)

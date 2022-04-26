from random import randint

DESCRIPTION = 'What number is missing in the progression?'
MIN_POSSIBLE_NUM = 1
MAX_POSSIBLE_NUM = 99


def generate_progression(first_num, step, progression_length):
    return [first_num + step * i for i in range(progression_length)]


def generate_round():
    first_number = randint(MIN_POSSIBLE_NUM, MAX_POSSIBLE_NUM)
    max_step = 9
    progression_length = 10
    question = ''
    step = randint(1, max_step)
    hidden_index = randint(1, progression_length)
    progression = generate_progression(first_number, step, progression_length)
    for i in range(len(progression)):
        if i == hidden_index - 1:
            question += '.. '
            result = str(progression[i])
        else:
            question += str(progression[i]) + ' '
    return question, result

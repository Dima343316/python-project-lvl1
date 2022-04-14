import prompt
import random


DESCRIPTION = "What number is missing in the progression?"


def rand_ind(lst):
    return random.randint(0, len(lst) - 1)


def list_text(lst):
    return(" ". join(map(str, lst)))


def generate_param():
    random_number = random.randint(0, 10)
    random_num = random.randint(15, 20)
    rn_1 = list(range(random_number, random_num))
    rn_3 = rand_ind(rn_1)
    que = str(rn_1[rn_3])
    rn_1[rn_3] = ".."
    question = list_text(rn_1)
    return question, str(que)






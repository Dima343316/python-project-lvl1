from math import gcd
import random
import prompt


DESCRIPTION = "Find the greatest common divisor of given numbers."

def generate_param():
    random_num = random.randint(0, 101)
    random_number = random.randint(0, 101)
    question = (str(random_num) + ' ' + str(random_number))
    divid = gcd(random_num, random_number)
    return question, str(divid)


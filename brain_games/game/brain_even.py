#!/usr/bin/env python
import random
from prompt_toolkit import prompt


def even_2():
    return "Let's try again, " + name + '!'


def even_3():
    return "Congratulations, " + name + '!'


def even_1():
    random_number = str(random.randint(0, 101))
    number = (' Question: ' + random_number)
    print(number)
    vvod = input(' Your answer: ')
    true = str('Correct!')
    if float(random_number) % 2 == 0 and vvod == 'yes' or float(random_number) % 2 != 0 and vvod == 'no':
        print(true)
        return even_3()
    else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        return even_2()


def even():
    random_number = str(random.randint(0, 101))
    number = ("Question: " + random_number)
    print(number)
    vvod = input('Your answer: ')
    true = str('Correct!')
    if float(random_number) % 2 == 0 and vvod == 'yes' or float(random_number) % 2 != 0 and vvod == 'no':
        print(true)
        return even_1()
    else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        return even_2()


def even_numbers():
    print('Welcome to the Brain Games!')
    global name
    name = prompt('May I have your name?: ')
    print('Hello,', name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    random_number = str(random.randint(0, 101))
    number = ("Question: " + random_number)
    print(number)
    vvod = input('Your answer: ')
    true = ('Correct!')
    if float(random_number) % 2 == 0 and vvod == 'yes' or float(random_number) % 2 != 0 and vvod == 'no':
        print(true)
        return even()
    else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        return even_2()

from math import gcd
import random
from prompt_toolkit import prompt


def even_2():
    return "Let's try again, " + name + '!'


def even_3():
    return "Congratulations, " + name + '!'


def gcd_3():
    global random_number
    random_number = random.randint(0, 101)
    global random_number_1
    random_number_1 = random.randint(0, 101)
    number = ("Question: " + str(random_number) + ' ' + str(random_number_1))
    print(number)
    answer = input('Your answer: ')
    divider = gcd(random_number, random_number_1)
    while str(answer) == str(divider):
        print('Correct!')
        return even_3()
    else:
        print((str(answer) + " is wrong answer ;(.
            Correct answer was " + str(divider)))
        return even_2()


def gcd_2():
    global random_number
    random_number = random.randint(0, 101)
    global random_number_1
    random_number_1 = random.randint(0, 101)
    number = ("Question: " + str(random_number) + ' ' + str(random_number_1))
    print(number)
    answer = input('Your answer: ')
    divider = gcd(random_number, random_number_1)
    while str(answer) == str(divider):
        print('Correct!')
        return gcd_3()
    else:
        print((str(answer) + " is wrong answer ;(."
                             " Correct answer was " + str(divider)))
        return even_2()


def gcd_1():
    print('Welcome to the Brain Games!')
    global name
    name = prompt('May I have your name?: ')
    print('Hello ,', name + '!')
    global random_number
    random_number = random.randint(0, 101)
    global random_number_1
    random_number_1 = random.randint(0, 101)
    print("Find the greatest common divisor of given numbers.")
    number = ("Question: " + str(random_number) + ' ' + str(random_number_1))
    print(number)
    answer = input('Your answer: ')
    divider = gcd(random_number, random_number_1)
    while str(answer) == str(divider):
        print('Correct!')
        return gcd_2()
    else:
        print(str(answer) + " is wrong answer ;(."
                            " Correct answer was " + str(divider))
        return even_2()


print(gcd_1())

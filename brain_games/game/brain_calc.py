import operator
import random
from prompt_toolkit import prompt


def even_2():
    return "Let's try again, " + name + '!'


def even_3():
    return "Congratulations, " + name + '!'


def calc_3():
    global random_num
    random_num = (random.randint(0, 101))
    global random_1
    random_1 = (random.randint(0, 101))
    signs = ['-', '*', '+']
    global sin
    sin = random.choice(signs)
    num = ("Question: " + str(random_num) + ' ' + sin + ' ' + str(random_1))
    print(num)
    ans = input('Your answer : ')
    funks = {'+': operator.add(random_num, random_1),
             '-': operator.sub(random_num, random_1),
             '*': operator.mul(random_num, random_1)}
    cal = funks[sin]
    while str(ans) == str(cal):
        print('Correct!')
        return even_3()
    else:
        print((str(ans) + "is wrong answer ;(. "
                          "Correct answer was" + str(cal)))
        return even_2()


def calc_2():
    global random_num
    random_num = (random.randint(0, 101))
    global random_1
    random_1 = (random.randint(0, 101))
    signs = ['-', '*', '+']
    global sin
    sin = random.choice(signs)
    num = ("Question: " + str(random_num) + ' ' + sin + ' ' + str(random_1))
    print(num)
    ans = input('Your answer: ')
    funks = {'+': operator.add(random_num, random_1),
             '-': operator.sub(random_num, random_1),
             '*': operator.mul(random_num, random_1)}
    cal = funks[sin]
    while str(ans) == str(cal):
        print('Correct!')
        return calc_3()
    else:
        print((str(ans) + "is wrong answer "
                          ";(. Correct answer was" + str(cal)))
        return even_2()


def calc_1():
    print('Welcome to the Brain Games!')
    global name
    name = prompt('May I have your name?: ')
    print('Hello,', name + '!')
    global random_num
    random_num = (random.randint(0, 101))
    global random_1
    random_1 = (random.randint(0, 101))
    signs = ['-', '*', '+']
    global sin
    sin = random.choice(signs)
    print("What is the result of the expression?")
    num = ("Question: " + str(random_num) + ' ' + sin + ' ' + str(random_1))
    print(num)
    ans = input('Your answer:')
    funks = {'+': operator.add(random_num, random_1),
             '-': operator.sub(random_num, random_1),
             '*': operator.mul(random_num, random_1)}
    cal = funks[sin]
    while str(ans) == str(cal):
        print('Correct!')
        return calc_2()
    else:
        print((str(ans) + "is wrong answer ;(."
                          " Correct answer was" + str(cal)))
        return even_2()


print(calc_1())

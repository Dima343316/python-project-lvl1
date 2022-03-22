import operator
import random
from prompt_toolkit import prompt


def even_2():
    return "Let's try again, " + name + '!'


def even_3():
    return "Congratulations, " + name + '!'


def calc_3():
    global random_number
    random_num =(random.randint(0, 101))
    global random_number_1
    random_num_1 =(random.randint(0, 101))
    signs = ['-', '*', '+']
    global singns_1
    singns_1 = random.choice(signs)
    number = ("Question: " +str(random_num) + ' ' + singns_1 + ' ' +str(random_num_1))
    print(number)
    answer = input('Your answer : ')
    funks = {'+': operator.add(random_num, random_num_1), '-': operator.sub(random_num, random_num_1), '*': operator.mul(random_num, random_num_1)}
    calculation = funks[singns_1]
    while str(answer) == str(calculation):
        print('Correct!')
        return even_3()
    else:
        print((str(answer) + " is wrong answer ;(. Correct answer was " + str(calculation)))
        return even_2()


def calc_2():
    global random_number
    random_num =(random.randint(0, 101))
    global random_number_1
    random_num_1 =(random.randint(0, 101))
    signs = ['-', '*', '+']
    global singns_1
    singns_1 = random.choice(signs)
    number = ("Question: " +str(random_num) + ' ' + singns_1 + ' ' +str(random_num_1))
    print(number)
    answer = input('Your answer: ')
    funks = {'+': operator.add(random_num, random_num_1), '-': operator.sub(random_num, random_num_1), '*': operator.mul(random_num, random_num_1)}
    calculation = funks[singns_1]
    while str(answer) == str(calculation):
        print('Correct!')
        return calc_3()
    else:
        print((str(answer) + "is wrong answer ;(. Correct answer was" + str(calculation)))
        return even_2()


def calc_1():
    print('Welcome to the Brain Games!')
    global name
    name = prompt('May I have your name?: ')
    print('Hello,', name + '!')
    global random_number
    random_num =(random.randint(0, 101))
    global random_number_1
    random_num_1 =(random.randint(0, 101))
    signs = ['-', '*', '+']
    global singns_1
    singns_1 = random.choice(signs)
    print("What is the result of the expression?")
    number = ("Question: " +str(random_num) + ' ' + singns_1 + ' ' +str(random_num_1))
    print(number)
    answer = input('Your answer:')
    funks = {'+': operator.add(random_num, random_num_1), '-': operator.sub(random_num, random_num_1), '*': operator.mul(random_num, random_num_1)}
    calculation = funks[singns_1]
    while str(answer) == str(calculation):
        print('Correct!')
        return calc_2()
    else:
        print((str(answer) + " is wrong answer ;(. Correct answer was " + str(calculation)))
        return even_2()


print(calc_1())

import random
from prompt_toolkit import prompt


def even_2():
    return "Let's try again, " + name + '!'


def even_3():
    return "Congratulations, " + name + '!'


def even(number):
    if number % 2 == 0:
        return "'yes'"
    elif number % 2 != 0:
        return "'no'"


def even_1():
    random_number = random.randint(0, 101)
    number = ('Question: ' + str(random_number))
    print(number)
    vvod = input('Your answer: ')
    proverka = even(random_number)
    if float(random_number)\
            % 2 == 0 and vvod == 'yes' or float(random_number)\
            % 2 != 0 and vvod == 'no':
        print('Correct!')
        return even_3()
    else:
        print((f"'{vvod}'")
              + " is wrong answer ;(. Correct answer was "
              + str(proverka))
        return even_2()


def even_5():
    random_number = random.randint(0, 101)
    number = ("Question: " + str(random_number))
    print(number)
    vvod = input('Your answer: ')
    proverka = even(random_number)
    if float(random_number)\
            % 2 == 0 and vvod == 'yes' or float(random_number)\
            % 2 != 0 and vvod == 'no':
        print('Correct!')
        return even_1()
    else:
        print((f"'{vvod}'")
              + " is wrong answer ;(. Correct answer was "
              + str(proverka))
        return even_2()


def even_numbers():
    print('Welcome to the Brain Games!')
    global name
    name = prompt('May I have your name?: ')
    print('Hello,', name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    random_number = random.randint(0, 101)
    number = ("Question: " + str(random_number))
    print(number)
    vvod = input('Your answer: ')
    proverka = even(random_number)
    if float(random_number)\
            % 2 == 0 and vvod == 'yes' or float(random_number)\
            % 2 != 0 and vvod == 'no':
        print('Correct!')
        return even_5()
    else:
        print((f"'{vvod}'")
              + " is wrong answer ;(. Correct answer was "
              + str(proverka))
        return even_2()


print(even_numbers())

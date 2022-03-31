from math import gcd
import random
import prompt


def even_2():
    return "Let's try again, " + name + '!'


def even_3():
    return "Congratulations, " + name + '!'


def gcd_1():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name?: ')
    print('Hello,', name + '!')
    print("Find the greatest common divisor of given numbers.")
    for i in range(3):
        global random_number
        random_num = random.randint(0, 101)
        global random_number_1
        random_number_1 = random.randint(0, 101)
        number = ("Question: " + str(random_num) + ' ' + str(random_number_1))
        print(number)
        answer = input('Your answer: ')
        divider = gcd(random_num, random_number_1)
        if str(answer) == str(divider):
            print('Correct!')
        else:
            print((f"'{(answer)}'") + " is wrong answer ;(."
                            " Correct answer was " + (f"'{(divider)}'"))
            return even_2()
    else:
        return even_3()


print(gcd_1())

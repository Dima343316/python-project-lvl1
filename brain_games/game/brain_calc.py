import operator
import random
import prompt


def even_2():
    return "Let's try again, " + name + '!'


def even_3():
    return "Congratulations, " + name + '!'


def calc_1():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name?: ')
    print('Hello,', name + '!')
    print("What is the result of the expression?")
    for i in range(3):
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
        if str(ans) == str(cal):
            print('Correct!')
        else:
            print((f"'{(ans)}'") + ' ' + 'is wrong answer ;(.'
                                         ' Correct answer'
                                         ' was' + ' ' + (f"'{(cal)}'"))
            return even_2()
    else:
        return even_3()


print(calc_1())

from prompt_toolkit import prompt
import random


def even_2():
    return "Let's try again, " + name + '!'


def even_3():
    return "Congratulations, " + name + '!'


def rand_ind(lst):
    return random.randint(0, len(lst) - 1)


def list_text(lst):
    return(" ". join(map(str, lst)))


def progress_2():
    random_number = random.randint(0, 15)
    random_num = random.randint(18, 21)
    rn_1 = list(range(random_number, random_num))
    rn_3 = rand_ind(rn_1)
    que = str(rn_1[rn_3])
    rn_1[rn_3] = ".."
    quest_1 = list_text(rn_1)
    print(("Question: ") + quest_1)
    ans = input('Your answer: ')
    while str(ans) == que:
        print('Correct!')
        return even_3()
    else:
        print(str(ans) + " is wrong answer ;(. Correct answer was " + str(que))
        return even_2()


def progress_1():
    random_number = random.randint(0, 15)
    random_num = random.randint(18, 21)
    rn_1 = list(range(random_number, random_num))
    rn_3 = rand_ind(rn_1)
    que = str(rn_1[rn_3])
    rn_1[rn_3] = ".."
    quest_1 = list_text(rn_1)
    print(("Question: ") + quest_1)
    ans = input('Your answer: ')
    while str(ans) == que:
        print('Correct!')
        return progress_2()
    else:
        print(str(ans) + " is wrong answer ;(. Correct answer was " + str(que))
        return even_2()


def progress():
    print('Welcome to the Brain Games!')
    global name
    name = prompt('May I have your name?: ')
    print('Hello ,', name + '!')
    random_number = random.randint(0, 15)
    random_num = random.randint(18, 21)
    rn_1 = list(range(random_number, random_num))
    rn_3 = rand_ind(rn_1)
    que = str(rn_1[rn_3])
    rn_1[rn_3] = ".."
    print("What number is missing in the progression?")
    quest_1 = list_text(rn_1)
    print(("Question: ") + quest_1)
    ans = input('Your answer: ')
    while str(ans) == que:
        print('Correct!')
        return progress_1()
    else:
        print(str(ans) + " is wrong answer ;(. Correct answer was " + str(que))
        return even_2()


print(progress())

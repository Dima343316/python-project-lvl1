import prompt
import random


def even_2():
    return "Let's try again, " + name + '!'


def even_3():
    return "Congratulations, " + name + '!'


def rand_ind(lst):
    return random.randint(0, len(lst) - 1)


def list_text(lst):
    return(" ". join(map(str, lst)))


def progress():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name?: ')
    print('Hello ,', name + '!')
    print("What number is missing in the progression?")
    for i in range(3):
        random_number = random.randint(0, 10)
        random_num = random.randint(15, 20)
        rn_1 = list(range(random_number, random_num))
        rn_3 = rand_ind(rn_1)
        que = str(rn_1[rn_3])
        rn_1[rn_3] = ".."
        quest_1 = list_text(rn_1)
        print(("Question: ") + quest_1)
        ans = input('Your answer: ')
        if str(ans) == que:
            print('Correct!')
        else:
            print((f'"{(ans)}"') + " is wrong answer ;(."
                                   " Correct answer was " + (f'"{(que)}"'))
            return even_2()
    else:
        return even_3()


print(progress())

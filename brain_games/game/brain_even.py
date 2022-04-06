import random
import prompt


def even(number):
    if number % 2 == 0:
        return "'yes'"
    elif number % 2 != 0:
        return "'no'"


def even_numbers_11():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name?: ')
    print('Hello,', name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        random_number = random.randint(0, 101)
        number = ("Question: " + str(random_number))
        print(number)
        vvod = input('Your answer: ')
        proverka = even(random_number)
        if float(random_number)\
            % 2 == 0 and vvod == 'yes' or float(random_number)\
                % 2 != 0 and vvod == 'no':
            print('Correct!')
        else:
            print((f"'{vvod}'") + " is wrong answer ;(."
                                  " Correct answer was " + str(proverka))
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")

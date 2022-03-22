from prompt_toolkit import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt('May I have your name?:')
    print('Hello ,',name + '!')

welcome_user()


def even_2():
    return "Let's try again, " + name + '!'


def even_3():
    return "Congratulations, " + name

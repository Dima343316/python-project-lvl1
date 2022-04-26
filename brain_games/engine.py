import prompt


NUMBER_OF_ROUNDS = 3


def ask(question):
    print('Question:', question)
    return input('Your answer: ')


def run_game(game):
    print('Welcome to the Brain Games!')
    player = prompt.string('May I have your name? ')
    print(f'Hello, {player}')
    print(game.DESCRIPTION)
    for i in range(NUMBER_OF_ROUNDS):
        question, answer = game.generate_round()
        user_answer = ask(question)
        if str(answer) == str(user_answer):
            print('Correct!')
        else:
            print("'" + str(user_answer) + "' is a wrong answer ;(.", end='')
            print(" Correct answer was '" + answer + "'")
            print(f"Let's try again, {player}!")
            break
    else:
        print(f"Congratulations, {player}!")

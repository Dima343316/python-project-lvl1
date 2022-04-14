#!/usr/bin/env python
from brain_games.game.cli import welcome_user, quest


def run_game(game):
    user_name = welcome_user()
    print(game.DESCRIPTION)
    for i in range(3):
        question, answer = game.generate_param()
        user_answer = quest(question)
        if str(answer) == str(user_answer):
            print('Correct!')
        else:
            print("'" + str(user_answer) + "' is a wrong answer ;(.", end='')
            print(" Correct answer was '" + answer + "'")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")

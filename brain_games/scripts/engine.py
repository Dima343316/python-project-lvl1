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
            print((f"'{(user_answer)}'") + ' ' + 'is wrong answer ;(.'
                                         ' Correct answer'
                                         ' was' + ' ' + (f"'{(answer)}'"))
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")


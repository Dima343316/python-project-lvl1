import random
import prompt


def is_prime(x):
    result = {True: 'yes', False: 'no'}
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return result[False]
    return result[True]


def start_prime():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        num = random.randint(2, 100)
        print(f"Question: {num}")
        ans = input("Your answer: ")
        number = is_prime(num)
        if number == ans:
            print("Correct!")
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{number}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")

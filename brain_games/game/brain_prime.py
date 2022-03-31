import random
import prompt


def start_prime():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        num = random.randint(2, 100)
        flag = "yes"
        print(f"Question: {num}")
        ans = input("Your answer: ")
        if num != 2:
            for i in range(2, num):
                if num % i == 0:
                    flag = "no"
                    break
        if ans == flag:
            print("Correct!")
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{flag}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


start_prime()

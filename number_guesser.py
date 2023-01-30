import random


print("Welcome to our number guesser game - you have 10 tries to get it right.")
difficulty = input(
    "Do you want easy (numbers from 1 - 50) or hard (numbers from 1-100)? (e/h) ")

while difficulty not in ["e", "h"]:
    print("Invalid input, please enter either 'e' for easy or 'h' for hard.")
    difficulty = input(
        "Do you want easy (numbers from 1 - 50) or hard (numbers from 1-100)? (e/h) ")


def user_guess():
    user = int(input("Enter your guess: "))
    return user


upper_bound = 100 if difficulty == "h" else 50


def computer_guess():
    computer_num = random.randrange(1, upper_bound + 1)
    return computer_num


guess_com = computer_guess()
counter = 0

while counter < 10:
    guess_user = user_guess()
    if guess_user > 50 and difficulty == "e":
        print("You selected easy, the max value is 50, try again. ")
    elif guess_user > 100 and difficulty == "h":
        print("You selected hard, the max value is 100, try again. ")

    else:
        print(f"Your guess is {guess_user}.")
        counter += 1
        if guess_com > guess_user:
            print(
                f"Too low! Guess again. You are on attempt {counter} out of 10.")
        elif guess_com < guess_user:
            print(
                f"Too high! Guess again. You are on attempt {counter} out of 10.")
        else:
            print(
                f"You got it, it took you {counter} tries and the computer's guess was {guess_com}.")
            break
else:
    print("You have run out of tries.")

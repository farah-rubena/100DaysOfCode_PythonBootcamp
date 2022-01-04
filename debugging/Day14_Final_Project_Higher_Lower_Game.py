from Day14_Final_Project_Higher_Lower_Game_GameData import data

from Day14_Final_Project_Higher_Lower_Game_Logo import logo, vs

import random

from os import system


def get_random_account():

    compare = random.randint(0, len(data) - 1)
    return data[compare]


# format data into printable format
def format_data(account):

    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"


# takes user guess and follower count of a and b and checks if the user got it right
def check_answer(user_guess, a_follower_count, b_follower_count):

    if a_follower_count > b_follower_count:
        return user_guess == "a"
    else:
        return user_guess == "b"


score = 0


# make the game repeatable

game_should_continue = True

# if the user is correct make sure account_b becomes account_a
account_b = get_random_account()

while game_should_continue:
    # generate random account from game data
    account_a = account_b
    account_b = get_random_account()
    if account_a == account_b:
        account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"VS: {format_data(account_b)}")

    # ask user for a guess
    user_guess = input("Who has more followers A or B: ").lower()

    # check if user is correct, before that get followe count
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

    # give user feedback
    # keep track of score
    if is_correct:
        score += 1
        print(f"You're right. Your current score is {score}")
    else:
        game_should_continue = False
        print(
            f"Sorry, that's wrong. Your overall score was {score}. Thankyou for playing."
        )

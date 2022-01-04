from Day14_Final_Project_Higher_Lower_Game_GameData import data

from Day14_Final_Project_Higher_Lower_Game_Logo import logo, vs

import random


def get_random_account():

    compare = random.randint(0, len(data) - 1)
    return data[compare]


def format_data(account):

    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"


account_a = get_random_account()
account_b = get_random_account()
if account_a == account_b:
    account_b = get_random_account()


print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"VS: {format_data(account_b)}")


user_guess = input("Who has more followers A or B: ").lower()

a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]

if 
import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice_list = [rock, paper, scissors]
user_choice = int(
    input("What do you want to choose?: Type 0 for Rock, 1 for Paper, 2 for Scissors")
)

if user_choice < 0 or user_choice > 2:
    print("Out of scope. Please selece a numver between 0 and 2")
    exit()
print(choice_list[user_choice])

computer_choice = random.randint(0, len(choice_list) - 1)

print(choice_list[computer_choice])

choice_matrix = [
    ["It's a draw", "You lose", "You win"],
    ["You win", "It's a draw", "You lose"],
    ["You lose", "You win", "It's a draw"],
]

print(choice_matrix[user_choice][computer_choice])

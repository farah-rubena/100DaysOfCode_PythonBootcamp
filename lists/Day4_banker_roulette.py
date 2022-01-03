import random

names_string = input("Give everybody's name, separated by a comma and a space: ").split(
    ", "
)

choice = random.choice(names_string)

print(f"{choice} is going to buy the meal today!!")

# Option 2


def banker_roulette(names_string):
    choice = random.choice(names_string)
    return f"{choice} is going to buy the meal today!"


names_string = input("Enter cmma sep names: ").split(",")
x = banker_roulette(names_string)
print(x)

# Option 3

names_string = input("Give everybody's name, separated by a comma and a space: ").split(
    ", "
)

random_choice = random.randint(0, len(names_string) - 1)

print(f"{names_string[random_choice]} will pay thr bill today")

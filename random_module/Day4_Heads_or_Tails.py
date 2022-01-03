import random

choice = random.randint(0, 1)

if choice == 1:
    print("Heads")
else:
    print("Tails")

# Solution 2


def coin_toss():
    random_choice = random.randint(0, 1)
    if random_choice == 1:
        return "Heads"
    return "Tails"


x = coin_toss()
print(x)

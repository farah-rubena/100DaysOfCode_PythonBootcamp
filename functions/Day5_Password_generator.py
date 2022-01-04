import random
import string

letters = list(string.ascii_letters)

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

special_char = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "~",
    "/",
    "<",
    ">",
    "?",
    '"',
    ":",
    ";",
    "|",
]

print("Welome to PyPassword Generator!!!")

satisfied = False

while not satisfied:
    total_letters = int(input("How many letters would you like in your password?: \n"))

    total_nums = int(input("How many numbers would you like?: \n"))

    total_symbols = int(input("How many symbols would you like?: \n"))

    password = []

    for _ in range(total_letters):
        password.append(random.choice(letters))

    for _ in range(total_nums):
        password.append(random.choice(nums))

    for _ in range(total_symbols):
        password.append(random.choice(special_char))

    # print("".join(password))

    random.shuffle(password)
    password = "".join(password)
    print(f"Collated password with length {len(password)} is:{password}")

    is_satisfied = input("Are you satisfied with the password?: ")
    if is_satisfied == "yes":
        satisfied = True
        password = "".join(password)
        print(f"Your password is {password}")
    else:
        password = ""

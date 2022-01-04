enemies = 1  # global scope


def increase_enemies():

    return f"Enemies inside the function {enemies + 2}"


x = increase_enemies()
print(x)  # 3

enemies = 1  # global scope


def increase_enemies():

    enemies = 2  # local scope
    print(f"Enemies inside the function {enemies}")


increase_enemies()
print(f"Enemies outside the function {enemies}")

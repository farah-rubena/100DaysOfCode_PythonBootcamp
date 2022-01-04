from os import system
from Day10_Calculator_logo import logo
import os

print(logo)


def add(first_num, next_num):
    return first_num + next_num


def sub(first_num, next_num):
    return first_num - next_num


def mul(first_num, next_num):
    return first_num * next_num


def divide(first_num, next_num):
    return first_num / next_num


def calculator():

    first_num = float(input("Enter the first num: "))

    operator_dict = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": divide,
    }

    for _ in operator_dict:
        print(_)

    continue_calculating = True

    while continue_calculating:

        operator = input("Pick an operation from the above line: ")
        next_num = float(input("Enter the next number: "))
        calculation_function = operator_dict[operator]
        answer = calculation_function(first_num, next_num)

        print(f"{first_num} {operator} {next_num} = {answer}")

        continue_again = input(
            "Type 'y' to continue calculation or 'n' to start a new calculation: "
        ).lower()
        if continue_again == "y":
            os.system("cls")
            first_num = answer
        else:
            continue_calculating = False
            calculator()


calculator()

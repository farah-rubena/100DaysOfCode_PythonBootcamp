number = int(input("Which number do you want to check?"))

if (
    number % 2 == 0
):  # code block was missing equality operator, had assignment operator instead
    print("This is an even number.")
else:
    print("This is an odd number.")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:  # or operator used instead of and
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)  # list constructor was used

def prime_checker(num):

    # prime no's are only divisible by 1 and itself
    is_Prime = True
    for _ in range(2, num):
        if num % _ == 0:
            is_Prime = False

    if is_Prime:
        print(f"{num} is a Prime Number")
    else:
        print(f"{num} is not a Prime Number")


n = int(input("Enter a number: "))
prime_checker(num=n)

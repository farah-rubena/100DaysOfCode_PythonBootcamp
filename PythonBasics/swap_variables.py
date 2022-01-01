a = input("Enter value for a: ")
b = input("Enter value for a: ")

# swap variables
swap = a
a = b
b = swap

print("a: " + a)
print("b: " + b)


# OR

a = input("Enter value for a: ")
b = input("Enter value for a: ")

a, b = b, a

print("a: " + a)
print("b: " + b)

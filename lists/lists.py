lst = ["apple", "banana", "cherry", "pumpkin", "abord"]
lst[1] = 1
print(lst)

lst.append("rusu")

print(lst)

# extend adds a whole bunch of items to the end of the list

lst2 = [
    1,
    2,
    3,
    4,
    5,
    6,
]

lst.extend(lst2)

print(lst)

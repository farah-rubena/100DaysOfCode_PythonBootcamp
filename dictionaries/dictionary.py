programming_dict = {
    "bug": "An error in the program the prevenets the program from running as expected",
    "function": "reusable piece of cod that can be called over and over again",
    "loop": "the actiob of doing somethign over and over again",
}

# retrievng values from a dict
print(programming_dict["bug"])

# ading new items to the dict
programming_dict["comment"] = "piece of data that is ognored by the interpretor"

print(programming_dict)

# empty dictionary

empty_dict = {}

# wipe an exisiting dict

programming_dict = {}
print(programming_dict)

# eding an item in a dict
programming_dict["bug"] = "farah"

print(programming_dict)

# print keys

for item in programming_dict:
    print(item)

# to print values

for item in programming_dict:
    print(programming_dict[item])

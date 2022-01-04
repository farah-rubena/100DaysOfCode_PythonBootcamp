# return marsk the end of a function
def format_name(fname, lname):
    if fname == "" or lname == "":
        return
    formatted_fname = fname.title()
    formatted_lname = lname.title()

    return f"{formatted_fname} {formatted_lname}"


fname = input("Enter the first name: ")
lname = input("Enter the last name: ")
x = format_name(fname, lname)
print(x)

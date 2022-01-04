def format_name(fname, lname):

    formatted_fname = fname.title()
    formatted_lname = lname.title()

    return f"{formatted_fname} {formatted_lname}"


x = format_name("angela", "ANGELA")
print(x)

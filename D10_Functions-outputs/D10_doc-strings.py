def format_name(f_name,l_name):
    """Takes a first and last name, and formats it to 
    return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "provide valid inputs"

    return (f"{f_name.title()} {l_name.title()}")

print(format_name("jorge","alt"))
print(format_name("samuel","fuENTES"))
print(format_name("",""))

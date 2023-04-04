# a basic function would be

def greet1():
    print("g'day Matt")
    print("lovely day\n")


# adding args to greet a particular person

def greet2(name, location):
    print(f"Hello {name}")
    print(f"How is the day in {location}?\n")

# 1st we are going to print the first function
greet1()


# a simple call can be for second function
greet2("Jack Bauer","Washington")

# using positional arguments we can prevent misplacing the arguments
greet2(location="Dallas", name="Rich Texan")
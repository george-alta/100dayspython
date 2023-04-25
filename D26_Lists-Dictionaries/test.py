# list comprehension
"""
new_numbers = [n*2 for n in range(1, 5)]
print(new_numbers)
"""

# another option, adding conditions

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# how to create a list just with short names

short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)

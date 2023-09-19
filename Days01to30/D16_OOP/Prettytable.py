from prettytable import PrettyTable
import random

table = PrettyTable()  # created a new object
print(table)

table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
table.align = "l"
print(table)

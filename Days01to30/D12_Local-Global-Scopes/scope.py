enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function {enemies}")

increase_enemies()
print(f"enemies outside function {enemies}")

# def drink_potion():
#     potion_strenght = 2
#     print(potion_strenght)

# drink_potion()
# print(potion_strenght) will throw an error



player_health = 10

def drink_potion():
    potion_strenght = 2
    print(player_health)
    # player_health += 2
    # print(player_health)
    # to use a global variable into the function, needs to be used as argument. then it needs to be returned.


drink_potion()
print(player_health)

#when using if/while/for, there are no new local scopes created.
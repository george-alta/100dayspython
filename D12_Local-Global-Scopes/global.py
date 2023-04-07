enemies = 1

def increase_enemies():
    global enemies #use this to import global variables into the function
    enemies +=1
    return enemies

print(enemies)
increase_enemies()
print(enemies)
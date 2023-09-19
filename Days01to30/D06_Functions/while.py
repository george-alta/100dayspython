#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

def turn_left():
    print("robot turns left")

def move():
    print("robot moves forward")

def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#for step in range(1,7):
#    jump()
    
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)


#if the goal flag is at a random position HURDLE 2
def at_goal():
    print("goal")

while not at_goal():
    jump()

#if the goal flag is at a random position and hurdles are random - HURDLE 3

""" jump changes a bit, now the initial move needs to be deleted.
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
"""

def front_is_clear():
    print("returns if there is no wall in front")

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

#if the goal flag is at a random position and hurdles are random, and hurdle height is also random - HURDLE 4

def right_is_clear():
    print("returns if there is no wall in right")

#jump needs to be redefined to see how long the jump has to be

def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
   
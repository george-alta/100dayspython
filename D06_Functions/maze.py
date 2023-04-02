#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_left():
    print("turn left")
def at_goal(): 
    print("at goal")
def move():
    print("move") 
def right_is_clear():
    print("right") 
def front_is_clear():
    print("front")

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

  

while not at_goal():
    if front_is_clear():
        move()
        # to prevent infinite square loops, after moving we check if the right path is clear, so we can prepare the next move avoiding a turn right loop
        if right_is_clear():
            turn_right()        
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
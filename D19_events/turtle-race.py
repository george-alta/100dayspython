from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

guess = screen.textinput(
    "Guess", "Who do you think is going to win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "black", "purple"]
all_turtles = []


for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(-230, 75-(turtle*30))
    all_turtles.append(new_turtle)

race_end = False
winner = ""
while not race_end:
    for competitor in all_turtles:
        steps = random.randint(0, 10)
        competitor.forward(steps)
        if competitor.xcor() >= 200:
            index = all_turtles.index(competitor)
            winner = colors[index]
            print(f"{winner} wins the race!")
            race_end = True

if guess == winner:
    print(f"you guessed it right! the winner is {winner}")
else:
    print(f"better luck next time. The winner was {winner}")
"""
tem = Turtle(shape="turtle")
tem.penup()
tem.goto(-230, 45)

tim = Turtle(shape="turtle")
tim.penup()
tim.goto(-230, 15)

tom = Turtle(shape="turtle")
tom.penup()
tom.goto(-230, -15)

tum = Turtle(shape="turtle")
tum.penup()
tum.goto(-230, -45)

tuz = Turtle(shape="turtle")
tuz.penup()
tuz.goto(-230, -75)
"""
screen.exitonclick()

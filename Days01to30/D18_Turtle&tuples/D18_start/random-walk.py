from turtle import Turtle, Screen
import random

colors = ["dark goldenrod", "dark olive green",
          "red", "blue", "black", "salmon", "green", "teal", "magenta", "violet", "yellow", "gold"]
tim = Turtle()
# tim.shape("turtle")
tim.pensize(5)
tim.speed(0)
for step in range(800):
    tim.pencolor(random.choice(colors))
    tim.forward(10)
    tim.right(90*random.randint(0, 3))

screen = Screen()
screen.exitonclick()

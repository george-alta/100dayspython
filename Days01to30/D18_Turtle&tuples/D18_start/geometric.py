from turtle import Turtle, Screen
import random

colors = ["dark goldenrod", "dark olive green",
          "red", "blue", "black", "salmon", "green", "teal", "magenta", "violet", "yellow", "gold"]
tim = Turtle()
tim.shape("turtle")
for sides in range(4, 20):
    # tim.pencolor(random.randint(0, 255), random.randint(
    # 0, 255), random.randint(0, 255))
    tim.pencolor(random.choice(colors))
    for i in range(sides):
        tim.forward(100)
        tim.right(360/sides)

screen = Screen()
screen.exitonclick()

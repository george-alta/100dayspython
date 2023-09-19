import turtle as t
import random

colors = ["dark goldenrod", "dark olive green",
          "red", "blue", "black", "salmon", "green", "teal", "magenta", "violet", "yellow", "gold"]
tim = t.Turtle()
t.colormode(255)
# tim.shape("turtle")
tim.pensize(5)
tim.speed(0)
for step in range(200):
    randcolor = (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    tim.pencolor(randcolor)
    tim.forward(10)
    tim.right(90*random.randint(0, 3))

screen = t.Screen()
screen.exitonclick()

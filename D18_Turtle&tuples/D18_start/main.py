from turtle import Turtle, Screen
# other alternative is -> from turtle import *
# This will import everything with the module, but is disencouraged because can make code difficult to read and follow

# modules can be aliases, eg
# import turtle as t
# import random as r
# r.choice([1,2,3])


tim = Turtle()
tim.shape("turtle")
tim.color("red")
for i in range(4):
    tim.forward(100)
    tim.right(90)


screen = Screen()
screen.exitonclick()

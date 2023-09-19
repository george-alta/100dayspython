from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
tim.color("red")
for i in range(20):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)


screen = Screen()
screen.exitonclick()

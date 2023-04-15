from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fw():
    tim.forward(10)


def move_bw():
    tim.backward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def clear():
    screen.resetscreen()
    # tim.setpos(0,0)
    # tim.setheading(0)


screen.listen()
screen.onkey(key="w", fun=move_fw)
screen.onkey(key="s", fun=move_bw)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()

from turtle import Turtle

SPEED = 40
SCREENLIMIT = 250 - SPEED/2


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        # since we inherit the turtle class, all that follows is self
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(location)

    def go_up(self):
        if (self.ycor() < 230):
            self.goto(self.xcor(), self.ycor()+SPEED)

    def go_down(self):
        if (self.ycor() > -230):
            self.goto(self.xcor(), self.ycor()-SPEED)

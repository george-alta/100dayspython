from turtle import Turtle
import random
import time

SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.xmove = SPEED
        self.ymove = SPEED
        self.movespeed = 0.1

    def move(self):
        new_position = (self.xcor()+self.xmove, self.ycor()+self.ymove)
        self.goto(new_position)

    def bounce(self):
        self.ymove *= -1

    def pong(self):
        self.xmove *= -1

    def reset(self):
        self.goto(0, 0)
        time.sleep(0.5)
        self.movespeed = 0.1
        self.xmove = SPEED * ((-1)**(random.randint(1, 2)))
        self.ymove = SPEED * ((-1)**(random.randint(1, 2)))

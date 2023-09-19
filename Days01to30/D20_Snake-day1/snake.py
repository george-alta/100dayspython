from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = "right"

    def create_snake(self):

        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.head != "right":
            self.segments[0].setheading(180)
            self.head = "left"

    def right(self):
        if self.head != "left":
            self.segments[0].setheading(0)
            self.head = "right"

    def up(self):
        if self.head != "down":
            self.segments[0].setheading(90)
            self.head = "up"

    def down(self):
        if self.head != "up":
            self.segments[0].setheading(270)
            self.head = "down"

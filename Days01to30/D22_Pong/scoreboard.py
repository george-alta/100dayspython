from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.leftscore = 0
        self.rightscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 200)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.leftscore} {self.rightscore}", align=ALIGNMENT,
                   font=FONT)

    def left_score(self):
        self.leftscore += 1
        self.clear()
        self.update_scoreboard()

    def right_score(self):
        self.rightscore += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

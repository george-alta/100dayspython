from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("blue")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_on = True

while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce()

    if ball.xcor() >= 330 and r_paddle.distance(ball.xcor(), ball.ycor()) < 50 and ball.xmove > 0:
        ball.pong()
        ball.movespeed *= 0.9
        print(ball.movespeed)

    if ball.xcor() <= 330 and l_paddle.distance(ball.xcor(), ball.ycor()) < 30 and ball.xmove < 0:
        ball.pong()
        ball.movespeed *= 0.9
        print(ball.movespeed)

    if ball.xcor() >= 390:
        print("left scores!")
        scoreboard.left_score()
        ball.reset()

    if ball.xcor() <= -390:
        print("right scores!")
        scoreboard.right_score()
        ball.reset()
screen.exitonclick()

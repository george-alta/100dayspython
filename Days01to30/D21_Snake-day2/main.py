from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

REFRESH = 0.1
COLISSION = 15

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_is_on:
    screen.update()
    time.sleep(REFRESH)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < COLISSION:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with walls
    if (snake.head.xcor() > 280) or (snake.head.xcor() < -280) or (snake.head.ycor() > 280) or (snake.head.ycor() < -280):
        scoreboard.game_over()
        game_is_on = False

    # detect collision with tail
    # if head collides with tail, game over
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
